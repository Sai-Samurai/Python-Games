import pygame
from TM_Images import screen
from TM_Classes import Narrator

narrator = Narrator(100, 100, 170, 70)

# GAME FONTS

# Game text font for differet situations
text_font = pygame.font.Font("Retro_Gaming.ttf", 11)
game_font = pygame.font.Font("freesansbold.ttf", 25)
other_text = pygame.font.Font("Retro_Gaming.ttf", 35)
loading_text = pygame.font.Font("Retro_Gaming.ttf", 45).render("Loading...", False,
                                                               (255, 255, 255))
over_game_text = pygame.font.Font("Retro_Gaming.ttf", 45).render("GAME OVER", False,
                                                                 (255, 255, 255))
win_game_text = pygame.font.Font("Retro_Gaming.ttf", 45).render("YOU WIN", False,
                                                                (255, 255, 255))
restart_game = pygame.font.Font("Retro_Gaming.ttf", 20).render("Press Enter to try again or press "
                                                               "Escape to quit the game", False,
                                                               (255, 255, 255))


# Wrapping text
# Function being able to separate the text by counting number of words and length they have
def wrap_text(text, font, max_width):
    words = text.split()  # Split the text into words
    wrapped_lines = []  # Creating an empty list to store the warped text
    current_line = ""  # Initialising a string to make the currrent line

    for word in words:
        # Adds the word to the current line and if width of total words if greater than the max_width, then the word
        # will be sent to the next line.
        if font.size(current_line + word)[0] <= max_width:
            current_line += word + " "
        else:
            wrapped_lines.append(current_line)
            current_line = word + " "
    # if there are any words left, then they will be just added to the line
    if current_line:
        wrapped_lines.append(current_line)

    return wrapped_lines


# Speech and speech bubble
text_data = [
    {
        "position": (narrator.rect.x + 140, narrator.rect.y - 65),
        "size": (400, 85),
        "text": ("Welcome explorer from the wilderness... I see you have stumbled into this world...\n Rest assured, "
                 "I am a friend to you, not a foe... Let me help you and get you back to your world by "
                 "getting you through this door I have here...\n I will show myself when the time is right.")
    },
    {
        "position": (800, narrator.rect.y - 35),
        "size": (225, 80),
        "text": (
            "Hahahaha... Did you really think I was going to let come to my universe!?\n You've been trapped! I'll let "
            "you die here unless you can escape my dungeon!")
    },
    {
        "position": (800, narrator.rect.y - 35),
        "size": (225, 65),
        "text": "I suggest you being careful... If you want to escape from me, try not to die in the lava."
    },
    {
        "position": (800, narrator.rect.y - 35),
        "size": (200, 110),
        "text": ("I almost forgot to inform that in some rooms I may have assigned some of my"
                 " soldiers.\n Touching them might not hurt you, but their fireballs will. I hope you die in their hands. "
                 "Hahahaha!")
    },
    {},
    {
        "position": (1088 - 400, 40),
        "size": (300, 75),
        "text": ("Oh! you are one lucky adventurer. Come through this door, it will lead you towards the exit. "
                 "\nIf you trust me... \n(there are 1 in 4 chances I set you back to the start).")
    },
    {
        "position": (1088 - 400, 40),
        "size": (300, 65),
        "text": (("I hope I almost got you there. I must say... you are a barve adventurer. "
                  "\nI don't have anything left to keep you from escaping."
                  "\nSee you next time..."))
    }
]


def display_text(text_index):
    bubble_info = text_data[text_index]
    bubbleX, bubbleY = bubble_info["position"]
    bubble_size = bubble_info["size"]
    text = bubble_info['text']

    pygame.draw.rect(screen, 'white', pygame.Rect(bubbleX, bubbleY, *bubble_size))

    wrapped_lines = wrap_text(text, text_font, bubble_size[0] - 10)

    for i, line in enumerate(wrapped_lines):
        screen.blit(text_font.render(line, True, 'black', None),
                    (bubbleX + 10, bubbleY + 10 + i * 10))
