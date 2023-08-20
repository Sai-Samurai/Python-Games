import pygame, sys
from pygame import Rect

# print(pygame.__version__)
# input()

# General setup
pygame.init()
clock = pygame.time.Clock()

YELLOW = (255, 255, 0)  # Horrific yellow for debugging rectangles
playerX, playerY = (241, 400)
block_size = 50
block_size2 = 50
min_y = 400  # Value according the game's ground level

# Making anything disappear
transapency = (0, 0, 0, 0)

# Background image
background = pygame.image.load("Final_background.png")
background_width, background_height = background.get_size()

# Blurred background image
blur_background = pygame.image.load("Blur_final_background.png")

# Dungeon image
dungeon = pygame.image.load("Final_dungeon_background.png")
dungeon_width, dungeon_height = dungeon.get_size()

# Screen appearance
screen_width = background_width
screen_height = background_height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TM Game')
bg_color = pygame.Color('black')

# New screen appearance
# Note: Need some aesthetic changes, looks... could be worse
dngn_screen_width = dungeon_width
dngn_screen_height = dungeon_height
dungeon_screen = pygame.Surface((dngn_screen_width, dngn_screen_height))
dungeon_screen.blit(dungeon, (0, 0))

# Game Text Font For Level
game_font = pygame.font.Font("freesansbold.ttf", 25)
other_text = pygame.font.Font("Retro_Gaming.ttf", 35)

# Player image
p_image = pygame.image.load("Final_player.png").convert_alpha()
player_image = pygame.transform.scale(p_image, (p_image.get_width() / 5, p_image.get_height() / 6.5))
player_rect = player_image.get_rect()

# Block image
b_image = pygame.image.load("Brick_texture.png").convert_alpha()
block_image = pygame.transform.smoothscale(b_image, (b_image.get_width() / 3.3, b_image.get_height() / 3.3))
block_rect = block_image.get_rect()

# Enemy image
e_image = pygame.image.load("enemy1.png").convert_alpha()
enemy_image = pygame.transform.scale(e_image, (e_image.get_width() / 2, e_image.get_height() / 3.36))
enemy_rect = enemy_image.get_rect()

# Door image
d_image = pygame.image.load("door.png").convert_alpha()
door_image = pygame.transform.scale(d_image, (d_image.get_width() / 1.5, d_image.get_height() / 1.5))
door_rect = door_image.get_rect()

# Lava image
l_image = pygame.image.load("lava.png").convert_alpha()
lava_image = pygame.transform.scale(l_image, (l_image.get_width(), l_image.get_height() * 4 / 3))
lava_rect = lava_image.get_rect()

# Coin image
c_image = pygame.image.load("coin.png").convert_alpha()
coin_image = pygame.transform.scale(c_image, (c_image.get_width(), c_image.get_height()))
coin_rect = coin_image.get_rect()


###################################################################################################################################

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
            screen.blit(player_image, player_rect)
        else:
            screen.blit(pygame.transform.flip(player_image, True, False),
                        player_rect)  # Flpis the player horizontally when moving left

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

        player_rect.x = self.x
        player_rect.midtop = (self.x + self.length / 2, self.y)

        if player_rect.midbottom >= (self.x + self.length / 2, self.y + self.height):
            player_rect.midtop = (self.x + self.length / 2, self.y)

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
        screen.blit(block_image, self.rect)

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

    def appear(self, screen):
        # pygame.draw.rect(screen, (92, 64, 51), self.rect)
        screen.blit(enemy_image, self.rect)


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
        screen.blit(lava_image, self.rect)


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
        pygame.draw.rect(screen, narcolor, self.rect)


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
            screen.blit(coin_image, self.rect)


# Exit
color = (100, 150, 200)
exitlength = 80
exitheight = 113


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
        screen.blit(door_image, self.rect)


###################################################################################################################################

# PLAYER'S ATTRIBUTES VALUES

# Offset for collisions
offset = 0.5

# Jumping
y_gravity = 1
jump_height = 20
y_velocity = jump_height
on_ground = True

# Moving
move_right = False
move_left = False
move_up = False
speed_x = 7.5

# Player
player = Player(playerX, playerY, 60, 96, player_rect)
player_sprite = pygame.sprite.Group(player)

# Lives
lives = 3

# Coin score
coin_score = 0

# BLOCK'S ATTRIBUTES VALUES

# Blocks
blocks_sprite = pygame.sprite.Group()

block1 = Blocks(400, 350, block_size, block_size2, block_rect)
block2 = Blocks(550, 350, block_size, block_size2, block_rect)
block3 = Blocks(250, 350, block_size, block_size2, block_rect)
block5 = Blocks(340, 310, block_size, block_size2, block_rect)
block6 = Blocks(460, 435, block_size, block_size2, block_rect)
block4 = Blocks(210, 300, block_size, block_size2, block_rect)

# blocks_sprite.add(block4, block6)#, block2, block3, block1, block5)

for block in blocks_sprite:
    block.rect.x = block.x2
    block.rect.y = block.y2


# Wrapping text
# Function being able to separate the text by counting number of words and length they have
def wrap_text(text, font, max_width):
    words = text.split()
    wrapped_lines = []
    current_line = ""

    for word in words:
        if font.size(current_line + word)[0] <= max_width:
            current_line += word + " "
        else:
            wrapped_lines.append(current_line)
            current_line = word + " "

    if current_line:
        wrapped_lines.append(current_line)

    return wrapped_lines


# NARRATOR ATTRIBUTES

# Attributes
narcolor = 'purple'
narrator = Narrator(100, 100, 170, 70)
# bubble = pygame.Rect(bubbleX, bubbleY, 215, 80)
text_font = pygame.font.Font("Retro_Gaming.ttf", 10)


# Speech and speech bubble
def text0():
    bubbleX, bubbleY = narrator.rect.x + 150, narrator.rect.y - 65
    pygame.draw.rect(screen, 'white', pygame.Rect(bubbleX, bubbleY, 250, 110))

    text = "Welcome explorer from the wilderness... I see you have stumbled into this world...\n Rest assured, I am of no harm... I am a friend to you, not a foe... Let me help you and get you back to your world by getting you through this door I have here...\n I will show myself when the time is right."

    wrapped_lines = wrap_text(text, text_font, 240)

    for i, line in enumerate(wrapped_lines):
        screen.blit(text_font.render(line, True, 'black', None), (bubbleX + 10, bubbleY + 10 + i * 10))


def text1():
    bubbleX, bubbleY = 800, narrator.rect.y - 35
    pygame.draw.rect(screen, 'white', pygame.Rect(bubbleX, bubbleY, 200, 80))

    text = "Hahahaha... Did you really think I was going to let come to my universe!?\n You've been trapped! I'll let you die here unless you can escape my dungeon!"

    wrapped_lines = wrap_text(text, text_font, 180)

    for i, line in enumerate(wrapped_lines):
        screen.blit(text_font.render(line, True, 'black', None), (bubbleX + 10, bubbleY + 10 + i * 10))


def text2():
    bubbleX, bubbleY = 800, narrator.rect.y - 35
    pygame.draw.rect(screen, 'white', pygame.Rect(bubbleX, bubbleY, 200, 50))

    text = "Be careful... If you want to escape from me, try not to die in the lava."

    wrapped_lines = wrap_text(text, text_font, 180)

    for i, line in enumerate(wrapped_lines):
        screen.blit(text_font.render(line, True, 'black', None), (bubbleX + 10, bubbleY + 10 + i * 10))


def text3():
    bubbleX, bubbleY = 800, narrator.rect.y - 35
    pygame.draw.rect(screen, 'white', pygame.Rect(bubbleX, bubbleY, 200, 80))

    text = "Ah and before I go get a nap, I almost forgot to inform that in some rooms I may have assigned some of my soldiers. I hope you die in their hands. Hahahaha!"

    wrapped_lines = wrap_text(text, text_font, 180)

    for i, line in enumerate(wrapped_lines):
        screen.blit(text_font.render(line, True, 'black', None), (bubbleX + 10, bubbleY + 10 + i * 10))


# EXIT ATTRIBUTES

# Levels
level = -1

# Exit Method
door0 = Exit(800, 380, exitlength, exitheight, color)  # y = 380 is placed correctly on the ground
door1 = Exit(400, 0, exitlength, exitheight, color)  # before: 400, 250
door2 = Exit(10, 400, exitlength, exitheight, color)
door3 = Exit(400, 200, exitlength, exitheight, color)  # before: 1000, 380

exit_sprite = pygame.sprite.Group(door0)

# MAIN SCREEN ATTRIBUTES (Introduction)

# It will have: level = -1, blur background, play button (initialize with key pressing)
# Optional: how to play button

# Start button
# outer rectangle
start_outer = pygame.Rect(screen_width / 2 - 125, screen_height / 2 - 50, 250, 100)

# inner rectangle
start_inner = pygame.Rect(screen_width / 2 - 75, screen_height / 2 - 25, 150, 50)

# text
start_text = other_text.render("START", False, (0, 0, 0))
starting_text = start_text.get_rect(center=(screen_width / 2, screen_height / 2))
start_text2 = pygame.font.Font("Retro_Gaming.ttf", 15).render("Press ENTER/RETURN to start the game", False, (0, 0, 0))
starting_text2 = start_text2.get_rect(center=(screen_width / 2, screen_height / 2 + 65))

# LOADING SCREEN ATTRIBUTES

loading_screen_x, loading_screen_y = 0, 0
loading_screen = pygame.Rect(loading_screen_x, loading_screen_y, screen_width, screen_height)
loading_text = pygame.font.Font("Retro_Gaming.ttf", 45).render("Loading...", False, (255, 255, 255))


def loading():
    pygame.draw.rect(screen, (0, 0, 0), loading_screen)
    loading_text_rect = loading_text.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(loading_text, loading_text_rect)
    pygame.display.flip()  # We forcefully update the screen in order to display the loading screen
    pygame.time.delay(
        2500)  # 2500 represents 2500 miliseconds --> 2 seconds and a half of displaying the loading screen


# ENEMIES

enemy1 = Enemy(850, 420, 30, 60)
enemy_group = pygame.sprite.Group()

# BULLETS

bullet = Bullet((915, 436), 7.5, 'red')
bullet_speed = 10
bullet_group = pygame.sprite.Group(bullet)
bullet_hit = 0

# DEATH ITEMS ATTRIBUTES

# Lava
lava = Death_Items(600, 486, 350, 70)
lava_group = pygame.sprite.Group()
lava_contact = 0

# GAME OVER

over_game = pygame.Rect(0, 0, screen_width, screen_height)
over_game_text = pygame.font.Font("Retro_Gaming.ttf", 45).render("GAME OVER", False, (255, 255, 255))
over_game_text_rect = over_game_text.get_rect(center=(screen_width / 2, screen_height / 2))


def game_over():
    pygame.draw.rect(screen, (0, 0, 0), over_game)
    screen.blit(over_game_text, over_game_text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)


def game_over_screen():
    # Game over screen displaying if the player lives count turn 0
    if lives == 0:
        game_over()
        player.rect.x = 241
        player.rect.y = min_y
        player.rect.x = player.x
        player.rect.y = player.y
        lava_group.remove(lava)
        player.stop_jumping()


# COINS ATTRIBUTES

coin1 = Coins(200, 430, 19, 22, coin_image)
coin2 = Coins(300, 430, 19, 22, coin_image)
coin3 = Coins(400, 430, 19, 22, coin_image)
coin_group = pygame.sprite.Group()
coin_list = [coin1, coin2, coin3]

for coin in coin_list:
    coin.rect.x = coin.x
    coin.rect.y = coin.y

########################################################## GAME LOOP ##################################################################

game_running = True
# Game loop
while game_running:

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                player.moving_right = True

            if event.key == pygame.K_LEFT:
                player.moving_left = True

            if event.key == pygame.K_SPACE:
                player.jumping = True
                print("SPACE")

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False

    # Small text attributes
    level_text = other_text.render("Level "f"{level}", False, (255, 255, 255))
    lives_text = other_text.render("Lives : "f"{lives}", False, (255, 255, 255))
    score_text = other_text.render("Score: "f"{coin_score}", False, (255, 255, 255))

    player.rect.x = player.x
    player.rect.y = player.y

    # Forces the player to have gravity applied to it (MAJOR ERROR)
    # if player.y < min_y:
    #    player.y += 5 * y_gravity

    # COLLISIONS
    player.x = player.rect.x
    blocks_hit_list = pygame.sprite.spritecollide(player, blocks_sprite, False)
    print("The return value is", pygame.sprite.spritecollide(player, blocks_sprite, False))
    print(player, blocks_sprite)

    print("The player is at ", player.x, player.y)
    print("Player rectangle is at ", player.rect.x, player.rect.y)
    print("Block is at ", block4.x2, block4.y2)
    if pygame.sprite.spritecollideany(player, blocks_sprite) is not None:
        print(524)
        if pygame.sprite.spritecollide(player, blocks_sprite, False):
            print(525)

            # Applies to all blocks
            for block in blocks_hit_list:
                vlocks = block

            # Working code tested with Janani
            if player.rect.bottom >= vlocks.rect.top >= player.rect.top:
                if player.rect.centerx + 15 > vlocks.rect.left and player.rect.centerx - 15 < vlocks.rect.right:  # Makes sure that the player doesn't fade through the block in order to activate the bottom collision using the center of the player
                    player.rect.bottom = vlocks.rect.top + offset
                    player.y = player.rect.y
                    print("AAAAAAAAAAAAAAAAAAAAAA")

            elif player.rect.top <= vlocks.rect.bottom <= player.rect.bottom:
                if vlocks.rect.left < player.rect.centerx < vlocks.rect.right:
                    player.rect.top = vlocks.rect.bottom - offset
                    player.y = player.rect.y
                    y_velocity = - y_gravity
                    jumping = False
                    print("top")

            if player.rect.right >= vlocks.rect.left >= player.rect.left:
                if player.rect.centerx < vlocks.rect.left:
                    player.rect.right = vlocks.rect.left
                    player.x = player.rect.x
                    if player.rect.y != min_y:
                        y_velocity = - y_gravity
                        jumping = False
                    print("right")

            if player.rect.left <= vlocks.rect.right <= player.rect.right:
                if player.rect.centerx > vlocks.rect.right:
                    player.rect.left = vlocks.rect.right
                    player.x = player.rect.x
                    if player.rect.y != min_y:
                        y_velocity = - y_gravity
                        jumping = False
                    print("left")

        else:
            print(530)

    player.animate()

    # Visuals
    # screen.blit(background, (0, 0))

    # Exit collisions
    exit_collisions = pygame.sprite.spritecollideany(player, exit_sprite) is not None

    if exit_collisions:
        screen.blit(background, (- 80000, 0))

        if pygame.sprite.spritecollide(player, exit_sprite, True):
            # Every door is specific to its level and in resulting, by turning the value to True, every element of
            # the exit_sprite group is deleted from the group after every collision. By doing so,  we just need to
            # add every diffeent door to every specific level using the method .add().
            screen.blit(dungeon, (0, 0))
            level = level + 1

    # Lava collision
    lava_collision = pygame.sprite.spritecollideany(player, lava_group) is not None

    if lava_collision:
        if pygame.sprite.spritecollide(player, lava_group, False):
            player.jumping = True

            # Increase lava_contact for every collision
            lava_contact += 1
            # For every 3 contacts, the remainder (%) of the division is == 0
            # The fourth contact then takes one life from the player
            if lava_contact % 16 == 0:
                lives -= 1

    # Coin collisions
    coin_collision = pygame.sprite.spritecollideany(player, coin_group) is not None
    if coin_collision:
        if pygame.sprite.spritecollide(player, coin_group, True):
            # next() goes throught the coin list and finds the first coin from the list of coins where the coin's rectangle overlaps with the player's rectangle
            collided_coin = next(
                coin for coin in coin_list if coin.rect.colliderect(player.rect))  # coin are still in the coin_list

            if not collided_coin.collected:  # now the coins that have collided are to be removed from the sprite group
                collided_coin.collected = True
                coin_score += 1
                coin_group.remove(collided_coin)

    # Bullet collision
    bullet_center = (bullet.center[0], bullet.center[1])
    # Creating a smaller hitbox for the bullet --> A square that's hypotenuse is 2* the radius of the circle --> It is in the circle
    bullet_collision_area = pygame.Rect(bullet_center[0] - bullet.radius, bullet_center[1] - bullet.radius,
                                        bullet.radius * 2, bullet.radius * 2)

    if player.rect.colliderect(bullet_collision_area):
        bullet.x = 915
        bullet_hit += 1
        if bullet_hit % 3 == 0:
            lives -= 1

    for block in blocks_sprite:
        vlocks = block
        if vlocks.rect.colliderect(bullet_collision_area):
            bullet.x = 915

    # Main menu (Level -1)
    if level == -1:
        screen.blit(blur_background, (0, 0))

        # Start button
        pygame.draw.rect(screen, (200, 150, 120), start_outer, border_radius=10)  # Can decide on color later
        pygame.draw.rect(screen, 'red', start_inner, border_radius=10)  # Same here for the color
        screen.blit(start_text, starting_text)
        screen.blit(start_text2, starting_text2)

        # for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                loading()
                level = level + 1

        player.x, player.y = 241, 400
        print(level)
        print(coin_score)




    # Level 0
    elif level == 0:
        blocks_sprite = pygame.sprite.Group()
        screen.blit(background, (0, 0))
        for sprite in player_sprite:
            sprite.appear(screen)
        for sprite in blocks_sprite:
            sprite.appear(screen)
        for sprite in exit_sprite:
            sprite.appear(screen)

        narrator.appear(screen)
        text0()

        print(level)
        screen.blit(level_text, (750, 20))

        # Switch level back
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                level = level - 1

        print(lives)
        print(coin_score)




    # Level 1
    elif level == 1:
        # Setting the screen
        # screen.fill(bg_color)
        screen.blit(dungeon_screen, (0, 0))

        # Updating manually the sprite groups
        pygame.sprite.Sprite.add(door1, exit_sprite)
        blocks_sprite.add(block4, block6)

        for coin in coin_list:
            if not coin.collected:  # if no collision is happening the coins should be added to the coin group
                coin_group.add(coin)
        coin_group.draw(screen)

        for sprite in player_sprite:
            sprite.appear(screen)
        for sprite in blocks_sprite:
            sprite.appear(screen)
        for sprite in exit_sprite:
            sprite.appear(screen)

            text1()

        print(level)
        screen.blit(level_text, (750, 20))

        screen.blit(score_text, (450, 20))

        print(coin_score)
        print(lives)





    # Level 2
    elif level == 2:
        # Setting the screen
        # screen.fill(bg_color)
        screen.blit(dungeon_screen, (0, 0))

        # Updating manually the sprite groups

        # Removing everything from the sprite groups
        blocks_sprite.remove(block4, block6)
        for coin in coin_list:
            if not coin.collected:  # if no collision is happening the coins should be added to the coin group
                coin_group.remove(coin)

        # Adding the elements for this level
        pygame.sprite.Sprite.add(door2, exit_sprite)
        blocks_sprite.add(block1, block3)
        lava_group.add(lava)

        lava.appear(screen)
        for sprite in player_sprite:
            sprite.appear(screen)
        for sprite in blocks_sprite:
            sprite.appear(screen)
        for sprite in exit_sprite:
            sprite.appear(screen)
        narrator.appear(screen)
        text2()

        print(level)
        screen.blit(level_text, (750, 20))

        print(lives)
        screen.blit(lives_text, (150, 20))

        game_over_screen()

        print(coin_score)


    # Level 3
    elif level == 3:
        screen.blit(dungeon_screen, (0, 0))

        # Updating the sprite groups manually

        # Removing sprites from previous level
        blocks_sprite.remove(block1, block3)
        lava_group.remove(lava)

        # Adding the sprites
        enemy_group.add(enemy1)
        blocks_sprite.add(block6)
        exit_sprite.add(door3)

        # Animations
        bullet.animate()
        for bad_guy in enemy_group:
            if bullet.x <= 0:
                bullet.x = 915

        bullet.appear(screen)
        enemy1.appear(screen)
        for sprite in player_sprite:
            sprite.appear(screen)
        for sprite in blocks_sprite:
            sprite.appear(screen)
        for sprite in exit_sprite:
            sprite.appear(screen)
        text3()

        screen.blit(level_text, (750, 20))
        screen.blit(score_text, (450, 20))
        screen.blit(lives_text, (150, 20))

        game_over_screen()



    elif level > 3:  # Or we can manually say: if level != 0 and level != 1 and level != 2 ...
        # screen.fill(bg_color)
        screen.blit(dungeon_screen, (0, 0))
        player.x, player.y = 500, 200
        for sprite in player_sprite:
            sprite.appear(screen)

        level_text = other_text.render("Level "f"{level}", True, (250, 250, 250))
        print(level)
        screen.blit(level_text, (750, 20))

    # Debugging the player's y coordinate
    '''
	The player only realizes that he is under the ground (y level above 400)
	only after 20 pixels before coming back to the ground.
	'''
    print(player.x, " = PLAYERS X", player.y, " = PLAYERS Y")
    print(block.x2, " = BLOCKS X", block.y2, " = BLOCKS Y")

    if player.y > min_y:
        player.y = min_y
        print("Player going down!!!")
        print(screen_width, screen_height)

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
