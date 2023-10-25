import pygame

from TM_Images import screen, screen_width, screen_height
from Texts import loading_text

pygame.font.init()


# MAIN SCREEN ATTRIBUTES (Introduction)

'''
 It will have: level = -1, blur background, play button (initialize with key pressing)
 Optional: how to play button
'''

# LOADING SCREEN ATTRIBUTES

loading_screen_x, loading_screen_y = 0, 0
loading_screen = pygame.Rect(loading_screen_x, loading_screen_y, screen_width, screen_height)


def loading():
    pygame.draw.rect(screen, (0, 0, 0), loading_screen)
    loading_text_rect = loading_text.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(loading_text, loading_text_rect)
    pygame.display.flip()  # We forcefully update the screen in order to display the loading screen
    pygame.time.delay(
        2500)  # 2500 represents 2500 miliseconds --> 2 seconds and a half of displaying the loading screen
