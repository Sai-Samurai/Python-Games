import pygame
from TM_Images import screen
from TM_Classes import Narrator

narrator = Narrator(100, 100, 170, 70)
# GAME FONTS
# Game Text Font For Level
text_font = pygame.font.Font("Retro_Gaming.ttf", 10)
game_font = pygame.font.Font("freesansbold.ttf", 25)
other_text = pygame.font.Font("Retro_Gaming.ttf", 35)
loading_text = pygame.font.Font("Retro_Gaming.ttf", 45).render("Loading...", False,
                                                               (255, 255, 255))
over_game_text = pygame.font.Font("Retro_Gaming.ttf", 45).render("GAME OVER", False,
                                                                 (255, 255, 255))


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


# Speech and speech bubble
def text0():
    bubbleX, bubbleY = narrator.rect.x + 140, narrator.rect.y - 90
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
    pygame.draw.rect(screen, 'white', pygame.Rect(bubbleX, bubbleY, 200, 110))

    text = "Ah and before I go get a nap, I almost forgot to inform that in some rooms I may have assigned some of my soldiers.\n Touching them might not hurt you, but their fireballs will. I hope you die in their hands. Hahahaha!"

    wrapped_lines = wrap_text(text, text_font, 180)

    for i, line in enumerate(wrapped_lines):
        screen.blit(text_font.render(line, True, 'black', None), (bubbleX + 10, bubbleY + 10 + i * 10))
