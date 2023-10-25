import pygame

# Imports of all different images

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
pygame.display.set_caption('Pixel Odyssey (TM Game)')
bg_color = pygame.Color('black')

# New screen appearance
dngn_screen_width = dungeon_width
dngn_screen_height = dungeon_height
dungeon_screen = pygame.Surface((dngn_screen_width, dngn_screen_height))
dungeon_screen.blit(dungeon, (0, 0))

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
lava_image = pygame.transform.scale(l_image, (l_image.get_width(), l_image.get_height() + 10))
lava_rect = lava_image.get_rect()

# Narrator image
n_image = pygame.image.load("narrator.png").convert_alpha()
narrator_image = pygame.transform.scale(n_image, (n_image.get_width() / (767 / 170), n_image.get_height() / 5.3))
narrator_rect = narrator_image.get_rect()

# Coin image
c_image = pygame.image.load("coin.png").convert_alpha()
coin_image = pygame.transform.scale(c_image, (c_image.get_width(), c_image.get_height()))
coin_rect = coin_image.get_rect()
