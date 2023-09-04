import pygame

from Texts import other_text
from TM_Images import screen_width, screen_height

# Start button
# outer rectangle
start_outer = pygame.Rect(screen_width / 2 - 125, screen_height / 2 - 50, 250, 100)

# inner rectangle
start_inner = pygame.Rect(screen_width / 2 - 75, screen_height / 2 - 25, 150, 50)

# text
start_text = other_text.render("START", False, (0, 0, 0))
starting_text = start_text.get_rect(center=(screen_width / 2, screen_height / 2))
start_text2 = pygame.font.Font("Retro_Gaming.ttf", 15).render("Press ENTER/RETURN to start the game",
                                                              False, (0, 0, 0))
starting_text2 = start_text2.get_rect(center=(screen_width / 2, screen_height / 2 + 65))
