import pygame

from Texts import other_text
from TM_Images import screen_width, screen_height, screen


# text
game_name = pygame.font.Font("Retro_Gaming.ttf", 55).render("PIXEL ODYSSEY", False,
                                                            (0, 0, 0))
game_name_rect = game_name.get_rect(center=(screen_width / 2, screen_height / 4))

start_text = pygame.font.Font("Retro_Gaming.ttf", 20).render("Press ENTER/RETURN to start the game",
                                                             False, (250, 250, 250))
starting_text = start_text.get_rect(center=(screen_width / 2, screen_height / 2 + 165))


def start_screen():
    # Start
    screen.blit(start_text, starting_text)
    screen.blit(game_name, game_name_rect)
