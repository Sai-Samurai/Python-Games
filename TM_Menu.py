import pygame
import pygame.gfxdraw


def draw_blur(screen):
    screen.fill((0, 0, 0))
    snapshot = pygame.Surface(screen.get_size())
    snapshot.blit(screen, (0, 0))
    snapshot.set_alpha(200)
    snapshot = pygame.transform.smoothscale(snapshot, (int(snapshot.get_width() / 10),
                                                       (int(snapshot.get_height() / 10))))
    snapshot = pygame.transform.smoothscale(snapshot, (int(snapshot.get_width() * 10),
                                                       (int(snapshot.get_height() * 10))))
    screen.blit(snapshot, (0, 0))


def draw_menu(screen, options, selected_option):
    for i, option in enumerate(options):
        text_color = (255, 255, 255) if i == selected_option else (100, 100, 100)
        text_surface = pygame.font.Font("Retro_Gaming.ttf", 36).render(option, True, text_color)
        menu_title_text = pygame.font.Font("Retro_Gaming.ttf", 42).render("Menu", False,
                                                                          (255, 255, 255))
        screen.blit(text_surface, (50, 150 + i * 50))
        screen.blit(menu_title_text, menu_title_text.get_rect(center=(1088 / 2, 50)))


def handle_menu(screen, menu_open, selected_option, options):
    menu_open = True
    additional_text = ""
    while menu_open:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)

                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)

                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        additional_text = "Press ENTER to restart the level"
                    elif selected_option == 1:
                        pass
                    elif selected_option == 2:
                        pass
                elif event.key == pygame.K_RETURN and selected_option == 0:
                    additional_text = "Restarting the level..."

                elif event.key == pygame.K_m:
                    menu_open = False

        draw_blur(screen)
        draw_menu(screen, options, selected_option)

        additional_surface = pygame.font.Font("Retro_Gaming.ttf", 18).render(additional_text, False,
                                                                             'white')
        screen.blit(additional_surface, (540, 200))

        pygame.display.flip()
    return selected_option
