import pygame

import TM_Images

pygame.font.init()

y_gravity = 1
jump_height = 20
blocks_sprite = pygame.sprite.Group()
narcolor = 'purple'
YELLOW = (255, 255, 0)  # Horrific yellow for debugging rectangles
speed_x = 7.5
bullet_speed = 10
lives = 3
min_y = 400


# Player
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, length, height, image):
        super().__init__()
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.y_velocity = jump_height
        self.image = image
        self.rect = pygame.Rect(x, y, length, height)
        self.facing_right = True

    def appear(self, screen):
        pygame.draw.rect(screen, YELLOW, self.rect)
        if self.facing_right:
            screen.blit(TM_Images.player_image, TM_Images.player_rect)
        else:
            screen.blit(pygame.transform.flip(TM_Images.player_image, True, False),
                        TM_Images.player_rect)  # Flpis the player horizontally when moving left

    def move_right(self):
        self.x += speed_x
        self.rect.x = self.x
        self.facing_right = True

    def move_left(self):
        self.x -= speed_x
        self.rect.x = self.x
        self.facing_right = False

    def stop_jumping(self):
        self.jumping = False
        self.y_velocity = jump_height

    def animate(self):
        if self.moving_left:
            self.move_left()
        if self.moving_right:
            self.move_right()

        if self.jumping:
            self.y -= self.y_velocity
            self.y_velocity -= y_gravity
            if self.y_velocity < - jump_height:
                self.stop_jumping()

        TM_Images.player_rect.x = self.x
        TM_Images.player_rect.midtop = (self.x + self.length / 2, self.y)

        if TM_Images.player_rect.midbottom >= (self.x + self.length / 2, self.y + self.height):
            TM_Images.player_rect.midtop = (self.x + self.length / 2, self.y)

    def updateplayer(self, x, y):
        self.x = x
        self.y = y


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

    # pygame.draw.rect(screen, (0, 0, 0), (self.x2, self.y2, self.block_size, self.block_size2))
    '''
    #No need for this because the blocks don't move
    def updateblocks(self, x2, y2):
        self.x2
        self.y2
    '''


# Enemies
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, length, height):
        super().__init__()
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.rect = pygame.Rect(x, y, length, height)
        # enemy_group.add(self)

    def appear(self, screen):
        # pygame.draw.rect(screen, (92, 64, 51), self.rect)
        screen.blit(TM_Images.enemy_image, self.rect)


# Enemy bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, center, radius, color):
        super().__init__()
        self.center = center
        self.x, self.y = center
        self.radius = radius
        self.color = color
        # bullet_group.add(self)

    def appear(self, screen):
        pygame.draw.circle(screen, self.color, self.center, self.radius)

    def animate(self):
        self.x -= bullet_speed
        self.center = (self.x, self.y)


# Death items, like lava, spikes, ...
class Death_Items(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # self.d_item = d_item
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
        # pygame.draw.rect(screen, narcolor, self.rect)
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
        self.collected = False  # the collision of the player and the coin is false

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
        # self.color = color
        self.exit_image = exit_image
        self.rect = pygame.Rect(x3, y3, exitlength, exitheight)

    # exit_sprite.add(self)

    def appear(self, screen):
        pygame.draw.rect(screen, (135, 206, 235), self.rect)
        screen.blit(TM_Images.door_image, self.rect)
