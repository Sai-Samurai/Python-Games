import pygame

from Button import start_screen
from Loading import loading
from TM_Classes import Player, Boundary, Blocks, Enemy, Bullet, Death_Items, Narrator, Coins, Exit
from TM_Images import player_rect, block_rect, screen_width, screen_height, coin_image, screen, blur_background, \
    background, dungeon, dungeon_screen
from Texts import text0, text1, text2, text3, text5, text6, other_text, over_game_text, win_game_text, restart_game

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

'''
How to read and comapre the blocks variables to what you find on the screen?
It is simple... Well..
You have first the name that starts by "block" to designate the variable's composition.
Then you have the number of the block designated by an easy method... The blocks with the smallest y value go first.If 
by any chance some blocks have the same y coordinate, the order will be determined by the smallest x value to the 
biggest. And then the same thing happens the the next bigger y coordinate.
And finally, the "level_number" tells which level does the block belong to.
Simple... Right?
'''

# For the first level:
block_1_level_1 = Blocks(510, 235, block_size, block_size2, block_rect)
block_2_level_1 = Blocks(560, 235, block_size, block_size2, block_rect)
block_3_level_1 = Blocks(835, 263, block_size, block_size2, block_rect)
block_4_level_1 = Blocks(885, 263, block_size, block_size2, block_rect)
block_5_level_1 = Blocks(935, 263, block_size, block_size2, block_rect)
block_6_level_1 = Blocks(250, 315, block_size, block_size2, block_rect)
block_7_level_1 = Blocks(300, 315, block_size, block_size2, block_rect)
block_8_level_1 = Blocks(350, 315, block_size, block_size2, block_rect)
block_9_level_1 = Blocks(100, 446, block_size, block_size2, block_rect)

# For the second level:
block_1_level_2 = Blocks(400, 327, block_size, block_size2, block_rect)
block_2_level_2 = Blocks(600, 380, block_size, block_size2, block_rect)

# For the third level
block_1_level_3 = Blocks(350, 376, block_size, block_size2, block_rect)
block_2_level_3 = Blocks(500, 376, block_size, block_size2, block_rect)
block_3_level_3 = Blocks(670, 411, block_size, block_size2, block_rect)
block_4_level_3 = Blocks(200, 446, block_size, block_size2, block_rect)

# For the fourth level
block_1_level_4 = Blocks(200, 158, block_size, block_size2, block_rect)
block_2_level_4 = Blocks(1015, 199, block_size, block_size2, block_rect)
block_3_level_4 = Blocks(0, 203, block_size, block_size2, block_rect)
block_4_level_4 = Blocks(50, 203, block_size, block_size2, block_rect)
block_5_level_4 = Blocks(100, 203, block_size, block_size2, block_rect)
block_6_level_4 = Blocks(150, 203, block_size, block_size2, block_rect)
block_7_level_4 = Blocks(400, 208, block_size, block_size2, block_rect)
block_8_level_4 = Blocks(50, 253, block_size, block_size2, block_rect)
block_9_level_4 = Blocks(330, 305, block_size, block_size2, block_rect)
block_10_level_4 = Blocks(1015, 324, block_size, block_size2, block_rect)
block_11_level_4 = Blocks(740, 380, block_size, block_size2, block_rect)
block_12_level_4 = Blocks(540, 380, block_size, block_size2, block_rect)
block_13_level_4 = Blocks(180, 415, block_size, block_size2, block_rect)

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
door1 = Exit(920, 150, exitlength, exitheight, color)
door2 = Exit(30, 380, exitlength, exitheight, color)
door3 = Exit(1020, 380, exitlength, exitheight, color)
door4 = Exit(10, 90, exitlength, exitheight, color)
door5 = Exit(980, 380, exitlength, exitheight, color)
door6 = Exit(30, 380, exitlength, exitheight, color)

exit_sprite = pygame.sprite.Group()

# ENEMIES

enemy_group = pygame.sprite.Group()
enemy1 = Enemy(850, 420, 30, 60)
enemy2 = Enemy(850, 300, 30, 60)

enemy3 = Enemy(980, 135, 30, 60)
enemy4 = Enemy(980, 260, 30, 60)

# BULLETS

bullet_group = pygame.sprite.Group()
bullet_speed = 10
bullet1 = Bullet((enemy1.x + 8 + enemy1.length / 2, enemy1.y - 10 + enemy1.height / 2), 7.5, 'red')
bullet2 = Bullet((enemy2.x + 8 + enemy2.length / 2, enemy2.y - 10 + enemy2.height / 2), 7.5, 'red')

bullet3 = Bullet((enemy3.x + 8 + enemy3.length / 2, enemy3.y - 10 + enemy3.height / 2), 7.5, 'red')
bullet4 = Bullet((enemy4.x + 8 + enemy4.length / 2, enemy4.y - 10 + enemy4.height / 2), 7.5, 'red')
bullet_hit = 0

# DEATH ITEMS ATTRIBUTES

# Lava
lava = Death_Items(350, 495, 350, 80.5)  # Best to try is x = 200
lava_group = pygame.sprite.Group()
lava_contact = 0

# COINS ATTRIBUTES

level_coins = {
    -2: [],
    -1: [],
    0: [],
    1: [(block_1_level_1.x2 + 16.5, block_1_level_1.y2 - 27, 19, 22, coin_image),
        (block_3_level_1.x2 + 16.5, block_3_level_1.y2 - 27, 19, 22, coin_image),
        (block_6_level_1.x2 + 16.5, block_6_level_1.y2 - 27, 19, 22, coin_image),
        (530, 450, 19, 22, coin_image)],
    2: [(block_1_level_2.x2 + 16.5, block_1_level_2.y2 - 27, 19, 22, coin_image),
        (block_2_level_2.x2 + 16.5, block_2_level_2.x2 - 27, 19, 22, coin_image)],
    3: [],
    4: [],
    5: [],
    6: [],
    7: []
}

for coin_data in level_coins[level]:
    # The * is a shortcut to seperating all sprites for a list
    coin = Coins(*coin_data)
    coin_groups[level].add(coin)
# Creating sprite groups for each level
coin_groups = {level: pygame.sprite.Group() for level in level_coins}

'''
coin1 = Coins(block_1_level_1.x2 + 16.5, block_1_level_1.y2 - 27, 19, 22, coin_image)
coin2 = Coins(block_3_level_1.x2 + 16.5, block_3_level_1.y2 - 27, 19, 22, coin_image)
coin3 = Coins(block_6_level_1.x2 + 16.5, block_6_level_1.y2 - 27, 19, 22, coin_image)
coin4 = Coins(530, 450, 19, 22, coin_image)
coin_group = pygame.sprite.Group()
coin_list = [coin1, coin2, coin3, coin4]
'''

for coin in coin_groups[level]:
    coin.rect.x = coin.x
    coin.rect.y = coin.y

# GAME OVER

over_game = pygame.Rect(0, 0, screen_width, screen_height)
over_game_text_rect = over_game_text.get_rect(center=(screen_width / 2, screen_height / 2))

# WIN
win_game = pygame.Rect(0, 0, screen_width, screen_height)
win_game_text_rect = win_game_text.get_rect(center=(screen_width / 2, screen_height / 2))

restart_game_rect = restart_game.get_rect(center=(screen_width / 2, screen_height / 2 + 50))

# Nested Groups

all_groups = pygame.sprite.Group(blocks_sprite, exit_sprite, enemy_group, bullet_group,
                                 lava_group, coin_groups[level])


def empty_all_groups():
    for sprite in all_groups:
        all_groups.remove(sprite)


def game_over():
    pygame.draw.rect(screen, (0, 0, 0), over_game)
    screen.blit(over_game_text, over_game_text_rect)
    screen.blit(restart_game, restart_game_rect)
    empty_all_groups()
    for coin in coin_groups[level]:
        coin.collected = False
    pygame.display.flip()


def game_won():
    pygame.draw.rect(screen, (0, 0, 0), win_game)
    screen.blit(win_game_text, win_game_text_rect)
    screen.blit(restart_game, restart_game_rect)
    empty_all_groups()
    for coin in coin_groups[level]:
        coin.collected = False
    pygame.display.flip()


# coin_list = [coin for coin in coin_data]

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
            player.y -= player.y_velocity
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
    coin_collision = pygame.sprite.spritecollideany(player, coin_groups[level]) is not None
    if coin_collision:
        collided_coin = pygame.sprite.spritecollide(player, coin_groups[level], True)
        if collided_coin:
            coin_list = [coin for coin in coin_groups[level]]
            for coin in coin_groups[level]:
                if coin.rect.colliderect(player.rect):
                    collided_coin = coin
            # collided_coins = next(
            #    coin for coin in coin_list if coin.rect.colliderect(player.rect) and not coin.collected
            # )

            if collided_coin:
                coin.collected = True
                coin_score += 1
                coin_groups[level].remove(coin)
                # level_coins[level].remove(collided_coin)

            # coin_list = [coin for coin in coin_list if not coin.collected]

        '''
                    # Find the first collided coin of the current level
        for coin_data in level_coins[level]:
            coin = Coins(*coin_data)
            if coin.rect.colliderect(player.rect):
                collided_coin = coin
                break
        
        
        
        next() goes throught the coin list and finds the first coin from the list of coins where the coin's 
        rectangle overlaps with the player's rectangle
        
    
        collided_coin = next(
            coin for coin in coin_list if coin.rect.colliderect(player.rect))  # coin are still in the coin_list
    
        if not collided_coin.collected:  # now the coins that have collided are to be removed from the sprite group
            collided_coin.collected = True
            coin_score += 1
            coin_group.remove(collided_coin)
            
        '''

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
                if level == 3 or level == 4:  # adding level number condition for the collision to be true
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

    # coin_groups[level].draw(screen)

    #####     ####     #####     #####     #####     #####     #####     #####     #####     #####     #####     #####
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
        start_screen()

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

        coin_list = [coin for coin in coin_groups[level]]
        for coin_data in level_coins[level]:
            # Creating a temporary coin object
            coin = Coins(*coin_data)
            if coin.collected:
                coin_groups[level].add(coin)
        coin_groups[level].draw(screen)

        '''
        for coin in coin_list:
            if not coin.collected:  # if no collision is happening the coins should be added to the coin group
                coin_group.add(coin)
        coin_group.draw(screen)
        '''

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
        blocks_sprite.empty()

        for coin_data in level_coins[level]:
            coin = Coins(*coin_data)
            if not coin.collected:
                coin_groups[level].add(coin)

        # Remove any previously uncollected coins from the current level's sprite group
        for coin in coin_groups[level]:
            if not coin.collected:
                coin_groups[level].remove(coin)

        '''
        for coin in coin_list:
            if not coin.collected:  # if no collision is happening the coins should be added to the coin group
                coin_group.remove(coin)
        '''

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
        screen.blit(score_text, (450, 20))
        screen.blit(lives_text, (150, 20))

        print(lives)

        print(coin_score)


    # Level 3
    elif level == 3:
        screen.blit(dungeon_screen, (0, 0))

        # Updating the sprite groups manually

        # Removing sprites from previous level
        blocks_sprite.empty()
        lava_group.empty()

        # Adding the sprites
        enemy_group.add(enemy1, enemy2)
        bullet_group.add(bullet1, bullet2)
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


    # Level 4
    elif level == 4:
        screen.blit(dungeon_screen, (0, 0))

        # Removing sprites from groups
        enemy_group.empty()
        bullet_group.empty()
        blocks_sprite.empty()

        # Adding sprites in the groups
        exit_sprite.add(door4)
        blocks_sprite.add(block_1_level_4, block_2_level_4, block_3_level_4, block_4_level_4, block_5_level_4,
                          block_6_level_4, block_7_level_4, block_8_level_4, block_9_level_4, block_10_level_4,
                          block_11_level_4, block_12_level_4, block_13_level_4)
        enemy_group.add(enemy3, enemy4)
        bullet_group.add(bullet3, bullet4)

        for bullets in bullet_group:
            bullets.animate()

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

        screen.blit(level_text, (750, 20))
        screen.blit(score_text, (450, 20))
        screen.blit(lives_text, (150, 20))


    # Level 5
    elif level == 5:
        # Setting the screen
        # screen.fill(bg_color)
        screen.blit(dungeon_screen, (0, 0))
        blocks_sprite.empty()
        enemy_group.empty()
        bullet_group.empty()

        # Updating manually the sprite groups
        pygame.sprite.Sprite.add(door5, exit_sprite)

        for sprite in exit_sprite:
            sprite.appear(screen)
        for sprite in player_sprite:
            sprite.appear(screen)

        text5()

        screen.blit(score_text, (450, 20))
        screen.blit(lives_text, (150, 20))



    elif level == 6:  # Or we can manually say: if level != 0 and level != 1 and level != 2 ...
        screen.blit(background, (0, 0))

        pygame.sprite.Sprite.add(door6, exit_sprite)

        for sprite in exit_sprite:
            sprite.appear(screen)
        for sprite in player_sprite:
            sprite.appear(screen)

        text6()


    # Winning screen
    elif level == 7:  # Or we can manually say: if level != 0 and level != 1 and level != 2 ...
        screen.blit(background, (0, 0))

        game_won()

        # for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                level = -1
                lives = 3
                coin_score = 0

                for door in exit_sprite:
                    exit_sprite.remove(door)

        player.x, player.y = 241, 400






    print(player.x, " = PLAYERS X", player.y, " = PLAYERS Y")
    # print(block.x2, " = BLOCKS X", block.y2, " = BLOCKS Y")

    if lives == 0:
        level = -2

    print(level)

    # To view the boundary
    # for sprite in boundaries:
    #    sprite.appear(screen)

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
