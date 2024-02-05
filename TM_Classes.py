import pygame

import TM_Images

pygame.font.init()

# Different variables addded
y_gravity = 0.4
jump_height = 10
blocks_sprite = pygame.sprite.Group()
narcolor = 'purple'
YELLOW = (255, 255, 0)  # Horrific yellow for debugging rectangles
bullet_speed = 10
lives = 3


# Player
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, length, height, image, rect):
        super().__init__()
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.original_image = image
        self.moving_right = False
        self.moving_left = False
        self.jumping = True
        self.y_velocity = 0
        self.speed_x = 4.5
        self.portal_collision = False

        # Flags to track block collision on each side
        self.collide_bottom = False
        self.collide_top = False
        self.collide_right = False
        self.collide_left = False

        #Flags to track portal collision on each side
        self.collide_bottom_portal = False
        self.collide_top_portal = False
        self.collide_right_portal = False
        self.collide_left_portal = False

        self.boundary_collide_bottom = False
        self.boundary_collidetop = False

        self.image = image
        self.rect = rect
        self.rect = pygame.Rect(x, y, length, height)
        self.facing_right = True

    def update(self, blocks_sprite, boundaries, portal_group):
        # self.animate()
        self.block_collisions(blocks_sprite)
        self.boundary_collisions(boundaries)
        self.portal_collisions(portal_group)
        self.side_borders()

        portal_collisons = pygame.sprite.spritecollide(self, portal_group, False)
        if portal_collisons:
            self.shrink()

    def appear(self, screen):
        pygame.draw.rect(screen, YELLOW, self.rect)  # --> It is the hitbox of the player
        if self.facing_right:
            screen.blit(self.image, self.rect)
        else:
            screen.blit(pygame.transform.flip(self.image, True, False),
                        self.rect)  # Flips the player horizontally when moving left

    def move_right(self):
        self.x += self.speed_x
        if not self.jumping:
            self.y = self.y + 1
            self.jumping = True
        self.rect.x = self.x
        self.facing_right = True

    def move_left(self):
        self.x -= self.speed_x
        if not self.jumping:
            self.y = self.y + 1
            self.jumping = True
        self.rect.x = self.x
        self.facing_right = False

    # This a method that Dr.Jane has come up with to make working collisions
    def start_jumping(self):
        if not self.jumping:
            self.jumping = True
            self.y_velocity = jump_height
            self.y -= self.y_velocity

    def stop_jumping(self, blocks_sprite):
        self.jumping = False
        self.y_velocity = 0
        self.y = blocks_sprite.rect.top - self.height

    def side_borders(self):
        if not self.portal_collision:
            if self.x + self.length >= 1088:
                self.x = 1088 - self.length
        if self.portal_collision:
            if self.x + self.length / 2 >= 1088:
                self.x = 1088 - self.length / 2
        if self.x <= 0:
            self.x = 0
        if self.y <= 0:
            self.y = 0

    def boundary_stop_jumping(self, boundary):
        self.jumping = False
        self.y_velocity = 0
        self.y = boundary.rect.top - self.height

    def animate(self, boundaries):
        if self.moving_left:
            self.move_left()
        if self.moving_right:
            self.move_right()

        if not self.portal_collision:
            if self.jumping:
                self.y_velocity -= y_gravity
                self.y -= self.y_velocity

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        TM_Images.player_rect.x = self.x
        TM_Images.player_rect.midtop = (self.x + self.length / 2, self.y)

        if TM_Images.player_rect.midbottom >= (self.x + self.length / 2, self.y + self.height):
            TM_Images.player_rect.midtop = (self.x + self.length / 2, self.y)

        #self.block_collisions(blocks_sprite)
        self.boundary_collisions(boundaries)
        #self.side_borders()

        if self.portal_collision:
            self.jumping = False
            self.y_velocity = 0
            #self.rect.bottom = min(496 - self.height, self.rect.bottom)
            #print(self.rect.bottom)
            self.y = self.rect.y
            self.x = self.rect.x

    def block_collisions(self, blocks_sprite):
        block = pygame.sprite.spritecollideany(self, blocks_sprite)

        if block:

            bottom_collision = self.rect.bottom > block.rect.top and self.y_velocity <= 0
            top_collision = self.rect.top < block.rect.bottom and self.y_velocity > 0
            right_collision = self.rect.right >= block.rect.left >= self.rect.left
            left_collision = self.rect.left <= block.rect.right <= self.rect.right

            self.collide_bottom = bottom_collision
            self.collide_top = top_collision
            self.collide_right = right_collision
            self.collide_left = left_collision

            if self.rect.centery < block.rect.top:
                if bottom_collision:
                    self.stop_jumping(block)

                    self.collide_right = False
                    self.collide_left = False

                    if right_collision or left_collision:
                        right_collision = False
                        left_collision = False

            if self.rect.centery > block.rect.bottom:
                if top_collision:
                    self.y = block.rect.bottom
                    self.y_velocity = 0

                    if right_collision or left_collision:
                        right_collision = False
                        left_collision = False

            if right_collision:
                self.x = block.rect.left - self.length
                self.y_velocity -= y_gravity
                self.jumping = False
                self.y_velocity = 0

            if left_collision:
                self.x = block.rect.right
                self.y_velocity -= y_gravity
                self.jumping = False
                self.y_velocity = 0

    def boundary_collisions(self, boundaries):
        boundary = pygame.sprite.spritecollideany(self, boundaries)

        if boundary:

            bottom_boundary_collision = self.rect.bottom > boundary.rect.top and self.y_velocity <= 0
            top_boundary_collision = self.rect.top < boundary.rect.bottom and self.y_velocity > 0

            self.boundary_collide_bottom = bottom_boundary_collision
            self.boundary_collidetop = top_boundary_collision

            if bottom_boundary_collision:
                self.boundary_stop_jumping(boundary)
            elif top_boundary_collision:
                self.y = boundary.rect.bottom
                self.y_velocity = 0

        '''
        Instead of making multiple collision detections of the same block and platform at the same time, what we can do 
        is to just make the "floor" a new class and and leave the collision of itself with player as one and then make new
        collisions that would then be considered by the player and not cause the issue we have.
    
        Issue info:
        The player can not handle multiple collisons at the same time coming from sprites of the "same class".
        '''

    def portal_collisions(self, portal_group):
        portal = pygame.sprite.spritecollideany(self, portal_group)

        if portal:

            self.portal_collision = True

            bottom_portal_collision = self.rect.bottom > portal.rect.top and self.y_velocity <= 0
            top_portal_collision = self.rect.top < portal.rect.bottom and self.y_velocity > 0
            right_portal_collision = self.rect.right <= portal.rect.left <= self.rect.left
            left_portal_collision = self.rect.left >= portal.rect.right >= self.rect.right

            self.collide_bottom_portal = bottom_portal_collision
            self.collide_top_portal = top_portal_collision
            self.collide_right_portal = right_portal_collision
            self.collide_left_portal = left_portal_collision

            if self.rect.centery < portal.rect.top:
                if bottom_portal_collision:
                    self.stop_jumping(portal)

                    self.collide_bottom_portal = False
                    self.collide_left_portal = False

                    if right_portal_collision or left_portal_collision:
                        right_portal_collision = False
                        left_portal_collision = False

            if self.rect.centery > portal.rect.bottom:
                if top_portal_collision:
                    self.y = portal.rect.bottom
                    self.y_velocity = 0

                    if right_portal_collision or left_portal_collision:
                        right_portal_collision = False
                        left_portal_collision = False

            # Maybe this bit of code is not necessary
            if right_portal_collision:
                self.x = portal.rect.left - self.length
                self.y_velocity -= y_gravity
                self.jumping = False
                self.y_velocity = 0

            if left_portal_collision:
                self.x = portal.rect.right
                self.y_velocity -= y_gravity
                self.jumping = False
                self.y_velocity = 0

            self.speed_x = 3
            self.shrink()
            # self.rect = pygame.Rect(self.x, self.y, self.length / 2, self.height / 2)

    def shrink(self):
        new_length = int(self.length / 2)
        new_height = int(self.height / 2)

        self.image = pygame.transform.scale(self.original_image, (new_length, new_height))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.y = 420
        self.rect.y = self.y


class Boundary(pygame.sprite.Sprite):
    def __init__(self, x, y, length, height):
        super().__init__()
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.rect = pygame.Rect(x, y, length, height)

    def appear(self, screen):
        pygame.draw.rect(screen, (0, 150, 255), self.rect)


'''
Using Dr.Jane's code to make the boundaries and collisions
'''


# Blocks
class Blocks(pygame.sprite.Sprite):
    def __init__(self, x2, y2, block_size, block_size2, texture):
        super().__init__()
        self.x2 = x2
        self.y2 = y2
        self.block_size = block_size
        self.block_size2 = block_size2
        self.rect = pygame.Rect(x2, y2, block_size, block_size2)
        blocks_sprite.add(self)
        self.texture = texture

    def appear(self, screen):
        pygame.draw.rect(screen, YELLOW, self.rect)
        screen.blit(TM_Images.block_image, self.rect)


# Enemies
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, length, height):
        super().__init__()
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.rect = pygame.Rect(x, y, length, height)

    def appear(self, screen):
        screen.blit(TM_Images.enemy_image, self.rect)


# Enemy bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, center, radius, color):
        super().__init__()
        self.center = center
        self.x, self.y = center
        self.radius = radius
        self.color = color

    def appear(self, screen):
        pygame.draw.circle(screen, self.color, self.center, self.radius)

    def animate(self):
        self.x -= bullet_speed
        self.center = (self.x, self.y)


# Death items
class Death_Items(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    def appear(self, screen):
        pygame.draw.rect(screen, (255, 204, 0), self.rect)
        screen.blit(TM_Images.lava_image, self.rect)


# Narrator / Main evil villain
class Narrator:
    def __init__(self, narX, narY, narlength, narheight):
        super().__init__()
        self.narX = narX
        self.narY = narY
        self.narlength = narlength
        self.narheight = narheight
        self.narcolor = narcolor
        self.rect = pygame.Rect(narX, narY, narlength, narheight)
        self.other_text = pygame.font.Font("Retro_Gaming.ttf", 15)
        self.current_dialogue = ""

    def appear(self, screen):
        screen.blit(TM_Images.narrator_image, self.rect)


# Coins
class Coins(pygame.sprite.Sprite):
    def __init__(self, x, y, length, height, image):
        super().__init__()
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.rect = pygame.Rect(x, y, length, height)
        self.image = image
        self.collected = False  # The collision of the player and the coin is false

    def appear(self, screen):
        if not self.collected:
            pygame.draw.rect(screen, YELLOW, self.rect)
            screen.blit(TM_Images.coin_image, self.rect)


class Exit(pygame.sprite.Sprite):
    def __init__(self, x3, y3, exitlength, exitheight, exit_image):
        super().__init__()
        self.x3 = x3
        self.y3 = y3
        self.exitlength = exitlength
        self.exitheight = exitheight
        self.exit_image = exit_image
        self.rect = pygame.Rect(x3, y3, exitlength, exitheight)

    def appear(self, screen):
        pygame.draw.rect(screen, (135, 206, 235), self.rect)
        screen.blit(TM_Images.door_image, (self.x3 - 10, self.y3, self.exitlength, self.exitheight))


class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y, length, height):
        super().__init__()
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.color = ['darkgreen', 'darkblue']
        self.rect = pygame.Rect(x, y, length, height)

    def appear(self, screen):
        pygame.draw.rect(screen, self.color[0], self.rect)
