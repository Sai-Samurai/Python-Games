import pygame

from TM_Images import screen, screen_width, screen_height
from Texts import over_game_text
import TM_Classes
from TM_Classes import lives

pygame.font.init()

# GAME OVER

over_game = pygame.Rect(0, 0, screen_width, screen_height)
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
