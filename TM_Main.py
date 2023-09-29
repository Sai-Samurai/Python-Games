import pygame

from Button import start_button
from Loading import loading
from TM_Classes import Player, Boundary, Blocks, Enemy, Bullet, Death_Items, Narrator, Coins, Exit
from TM_Images import player_rect, block_rect, screen_width, screen_height, coin_image, screen, blur_background, \
    background, dungeon, dungeon_screen
from Texts import text0, text1, text2, text3, other_text, over_game_text, restart_game

# General setup
pygame.init()
clock = pygame.time.Clock()

######################################################################################################################

# PLAYER'S ATTRIBUTES VALUES

# Offset for collisions
offset = 0.5
flag = False

# Jumping
y_gravity = 1
jump_height = 20
y_velocity = jump_height
on_ground = True
# min_y = 400  # Value according the game's ground level

# Moving
move_right = False
move_left = False
move_up = False
speed_x = 7.5

# Player
playerX, playerY = (241, 400)
player = Player(playerX, playerY, 50, 96, player_rect)
player_sprite = pygame.sprite.Group(player)

# Lives
lives = 3

# Coin score
coin_score = 0

# BLOCK'S ATTRIBUTES VALUES

# Blocks
block_size = 50
block_size2 = 50
blocks_sprite = pygame.sprite.Group()

# Seperating the blocks and creating far mor entities for each level

# For the first level:

block_1_level_1 = Blocks(100, 446, block_size, block_size2, block_rect)
block_2_level_1 = Blocks(250, 315, block_size, block_size2, block_rect)
block_3_level_1 = Blocks(300, 315, block_size, block_size2, block_rect)
block_4_level_1 = Blocks(350, 315, block_size, block_size2, block_rect)
block_5_level_1 = Blocks(510, 235, block_size, block_size2, block_rect)
block_6_level_1 = Blocks(560, 235, block_size, block_size2, block_rect)
block_7_level_1 = Blocks(835, 263, block_size, block_size2, block_rect)
block_8_level_1 = Blocks(885, 263, block_size, block_size2, block_rect)
block_9_level_1 = Blocks(935, 263, block_size, block_size2, block_rect)

'''
block_1_level_1 = Blocks(790, 446, block_size, block_size2, block_rect)
block_2_level_1 = Blocks(650, 315, block_size, block_size2, block_rect)
block_3_level_1 = Blocks(600, 315, block_size, block_size2, block_rect)
block_4_level_1 = Blocks(550, 315, block_size, block_size2, block_rect)
block_5_level_1 = Blocks(350, 235, block_size, block_size2, block_rect)
block_6_level_1 = Blocks(300, 235, block_size, block_size2, block_rect)
block_7_level_1 = Blocks(135, 263, block_size, block_size2, block_rect)
block_8_level_1 = Blocks(85, 263, block_size, block_size2, block_rect)
block_9_level_1 = Blocks(35, 263, block_size, block_size2, block_rect)

'''


# For the second level:
block_1_level_2 = Blocks(400, 327, block_size, block_size2, block_rect)
block_2_level_2 = Blocks(600, 380, block_size, block_size2, block_rect)


# For the third level
block_1_level_3 = Blocks(200, 446, block_size, block_size2, block_rect)
block_2_level_3 = Blocks(350, 376, block_size, block_size2, block_rect)
block_3_level_3 = Blocks(500, 376, block_size, block_size2, block_rect)
block_4_level_3 = Blocks(670, 411, block_size, block_size2, block_rect)


for block in blocks_sprite:
    block.rect.x = block.x2
    block.rect.y = block.y2

# Boundaries
boundaries = pygame.sprite.Group([
    Boundary(0, 496, 1090, 40)
])

# NARRATOR ATTRIBUTES

# Attributes
narrator = Narrator(100, 100, 170, 70)
# bubble = pygame.Rect(bubbleX, bubbleY, 215, 80)


# EXIT ATTRIBUTES

# Levels
level = -1

# Exit

color = (100, 150, 200)
exitlength = 65
exitheight = 113

door0 = Exit(980, 380, exitlength, exitheight, color)  # y = 380 is placed correctly on the ground
door1 = Exit(920, 150, exitlength, exitheight, color)  # before: 400, 0
door2 = Exit(30, 380, exitlength, exitheight, color)
door3 = Exit(1020, 380, exitlength, exitheight, color)  # before: 400, 200

exit_sprite = pygame.sprite.Group()

# ENEMIES

enemy_group = pygame.sprite.Group()
enemy1 = Enemy(850, 420, 30, 60)
enemy2 = Enemy(850, 300, 30, 60)

# BULLETS

bullet_group = pygame.sprite.Group()
bullet_speed = 10
bullet = Bullet((enemy1.x + 8 + enemy1.length / 2, enemy1.y - 10 + enemy1.height / 2), 7.5, 'red')
bullet2 = Bullet((enemy2.x + 8 + enemy2.length / 2, enemy2.y - 10 + enemy2.height / 2), 7.5, 'red')
bullet_hit = 0

# DEATH ITEMS ATTRIBUTES

# Lava
lava = Death_Items(350, 495, 350, 80.5)  # Best to try is x = 200
lava_group = pygame.sprite.Group()
lava_contact = 0

# COINS ATTRIBUTES

coin1 = Coins(block_1_level_1.x2 + 16.5, block_1_level_1.y2 - 27, 19, 22, coin_image)
coin2 = Coins(block_3_level_1.x2 + 16.5, block_3_level_1.y2 - 27, 19, 22, coin_image)
coin3 = Coins(block_6_level_1.x2 + 16.5, block_6_level_1.y2 - 27, 19, 22, coin_image)
coin4 = Coins(530, 450, 19, 22, coin_image)
coin_group = pygame.sprite.Group()
coin_list = [coin1, coin2, coin3, coin4]

for coin in coin_list:
    coin.rect.x = coin.x
    coin.rect.y = coin.y

# GAME OVER

over_game = pygame.Rect(0, 0, screen_width, screen_height)
over_game_text_rect = over_game_text.get_rect(center=(screen_width / 2, screen_height / 2))

restart_game_rect = restart_game.get_rect(center=(screen_width / 2, screen_height / 2 + 50))

# Nested Groups

all_groups = pygame.sprite.Group(blocks_sprite, exit_sprite, enemy_group, bullet_group,
                                 lava_group, coin_group)


def empty_all_groups():
    for sprite in all_groups:
        all_groups.remove(sprite)


def game_over():
    pygame.draw.rect(screen, (0, 0, 0), over_game)
    screen.blit(over_game_text, over_game_text_rect)
    screen.blit(restart_game, restart_game_rect)
    empty_all_groups()
    for coin in coin_list:
        coin.collected = False
    pygame.display.flip()


######################################################################################################################
'''
Comment section if needed
'''
###################################################### GAME LOOP ####################################################

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
                player.start_jumping()
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

    player.animate()
    player.update(blocks_sprite, boundaries)

    player.rect.x = player.x
    player.rect.y = player.y

    # COLLISIONS
    player.x = player.rect.x
    blocks_hit_list = pygame.sprite.spritecollide(player, blocks_sprite, False)
    print("The return value is", pygame.sprite.spritecollide(player, blocks_sprite, False))
    print(player, blocks_sprite)

    print("The player is at ", player.x, player.y)
    print("Player rectangle is at ", player.rect.x, player.rect.y)
    print("Block is at ", block_2_level_1.x2, block_2_level_1.y2)

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
            player.start_jumping()

            # Increase lava_contact for every collision
            lava_contact += 1
            # For every 3 contacts, the remainder (%) of the division is == 0
            # The fourth contact then takes one life from the player
            if lava_contact % 4 == 0:
                lives -= 1

    # Coin collisions
    coin_collision = pygame.sprite.spritecollideany(player, coin_group) is not None
    if coin_collision:
        if pygame.sprite.spritecollide(player, coin_group, True):
            '''
            next() goes throught the coin list and finds the first coin from the list of coins where the coin's 
            rectangle overlaps with the player's rectangle
            '''

            collided_coin = next(
                coin for coin in coin_list if coin.rect.colliderect(player.rect))  # coin are still in the coin_list

            if not collided_coin.collected:  # now the coins that have collided are to be removed from the sprite group
                collided_coin.collected = True
                coin_score += 1
                coin_group.remove(collided_coin)

    # Bullet collision
    for projectiles in bullet_group:
        for monsters in enemy_group:
            bullet_center = (projectiles.center[0], projectiles.center[1])
            """
            Creating a smaller hitbox for the bullet 
            --> A square that's hypotenuse is 2* the radius of the circle 
            --> It is in the circle
            """
            bullet_collision_area = pygame.Rect(bullet_center[0] - projectiles.radius,
                                                bullet_center[1] - projectiles.radius, projectiles.radius * 2,
                                                projectiles.radius * 2)

            if player.rect.colliderect(bullet_collision_area):
                if level == 3:  # adding level number condition for the collision to be true
                    projectiles.x = monsters.x + 8 + monsters.length / 2
                    bullet_hit += 1
                    if bullet_hit % 3 == 0:
                        lives -= 1

            for block in blocks_sprite:
                vlocks = block
                if vlocks.rect.colliderect(bullet_collision_area):
                    projectiles.x = monsters.x + 8 + monsters.length / 2

            if projectiles.x <= 0:
                projectiles.x = monsters.x + 8 + monsters.length / 2



    # Game over (Level -2)
    if level == -2:
        game_over()

        # for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                level = level + 1
                lives = 3
                coin_score = 0

                for door in exit_sprite:
                    exit_sprite.remove(door)

        player.x, player.y = 241, 400


    # Main menu (Level -1)
    if level == -1:
        screen.blit(blur_background, (0, 0))
        start_button()

        # for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                loading()
                level = level + 1

        player.x, player.y = 241, 400

        print(coin_score)


    # Level 0
    elif level == 0:
        blocks_sprite = pygame.sprite.Group()
        pygame.sprite.Sprite.add(door0, exit_sprite)

        screen.blit(background, (0, 0))
        for sprite in blocks_sprite:
            sprite.appear(screen)
        for sprite in exit_sprite:
            sprite.appear(screen)
        for sprite in player_sprite:
            sprite.appear(screen)

        narrator.appear(screen)
        text0()

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
        blocks_sprite.add(block_1_level_1, block_2_level_1, block_3_level_1, block_4_level_1, block_5_level_1,
                          block_6_level_1, block_7_level_1, block_8_level_1, block_9_level_1)

        for coin in coin_list:
            if not coin.collected:  # if no collision is happening the coins should be added to the coin group
                coin_group.add(coin)
        coin_group.draw(screen)

        for sprite in blocks_sprite:
            sprite.appear(screen)
        for sprite in exit_sprite:
            sprite.appear(screen)
        for sprite in player_sprite:
            sprite.appear(screen)

            text1()

        screen.blit(level_text, (750, 20))

        screen.blit(score_text, (450, 20))

        screen.blit(lives_text, (150, 20))

        print(coin_score)
        print(lives)





    # Level 2
    elif level == 2:
        # Setting the screen
        # screen.fill(bg_color)
        screen.blit(dungeon_screen, (0, 0))

        # Updating manually the sprite groups

        # Removing everything from the sprite groups
        blocks_sprite.remove(block_1_level_1, block_2_level_1, block_3_level_1, block_4_level_1,
                             block_5_level_1, block_6_level_1, block_7_level_1, block_8_level_1, block_9_level_1)
        for coin in coin_list:
            if not coin.collected:  # if no collision is happening the coins should be added to the coin group
                coin_group.remove(coin)

        # Adding the elements for this level
        pygame.sprite.Sprite.add(door2, exit_sprite)
        blocks_sprite.add(block_1_level_2, block_2_level_2)
        lava_group.add(lava)

        lava.appear(screen)
        for sprite in blocks_sprite:
            sprite.appear(screen)
        for sprite in exit_sprite:
            sprite.appear(screen)
        for sprite in player_sprite:
            sprite.appear(screen)

        text2()

        screen.blit(level_text, (750, 20))

        print(lives)
        screen.blit(lives_text, (150, 20))

        print(coin_score)


    # Level 3
    elif level == 3:
        screen.blit(dungeon_screen, (0, 0))

        # Updating the sprite groups manually

        # Removing sprites from previous level
        blocks_sprite.remove(block_1_level_2, block_2_level_2)
        lava_group.remove(lava)

        # Adding the sprites
        enemy_group.add(enemy1, enemy2)
        bullet_group.add(bullet, bullet2)
        blocks_sprite.add(block_1_level_3, block_2_level_3, block_3_level_3, block_4_level_3)
        exit_sprite.add(door3)

        # Animations for all bullet sprites
        for bullet in bullet_group:
            bullet.animate()

        for sprite in blocks_sprite:
            sprite.appear(screen)
        for sprite in enemy_group:
            sprite.appear(screen)
        for sprite in exit_sprite:
            sprite.appear(screen)
        for sprite in bullet_group:
            sprite.appear(screen)
        for sprite in player_sprite:
            sprite.appear(screen)
        text3()

        screen.blit(level_text, (750, 20))
        screen.blit(score_text, (450, 20))
        screen.blit(lives_text, (150, 20))



    elif level == 4:  # Draft for further levels
        screen.blit(dungeon_screen, (0, 0))

        # Removing sprites from groups
        enemy_group.remove(enemy1)
        bullet_group.remove(bullet)
        blocks_sprite.remove(block_1_level_1)
        exit_sprite.remove(door3)

        for sprite in player_sprite:
            sprite.appear(screen)

        screen.blit(level_text, (750, 20))
        screen.blit(score_text, (450, 20))
        screen.blit(lives_text, (150, 20))


    elif level > 4:  # Or we can manually say: if level != 0 and level != 1 and level != 2 ...
        # screen.fill(bg_color)
        screen.blit(dungeon_screen, (0, 0))
        player.x, player.y = 500, 200
        for sprite in player_sprite:
            sprite.appear(screen)

        level_text = other_text.render("Level "f"{level}", True, (250, 250, 250))

        screen.blit(level_text, (750, 20))

    print(player.x, " = PLAYERS X", player.y, " = PLAYERS Y")
    # print(block.x2, " = BLOCKS X", block.y2, " = BLOCKS Y")

    if lives == 0:
        level = -2

    print(level)
    # for sprite in boundaries:
    #    sprite.appear(screen)

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
