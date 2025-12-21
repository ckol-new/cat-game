import pygame
import pygame_gui
from pygame_gui.elements.ui_button import UIButton
from cat_game.View.ScreenParameters import ScreenParameters



class Menu:
    def __init__(self, size=(ScreenParameters.PREF_WIDTH, ScreenParameters.PREF_HEIGHT)):
        pygame.init()
        self.__size = size
        self.__width = size[0]
        self.__height = size[1]
        self.__margin = 20
        self.__padding = 20
        self.__button_width = 80
        self.__button_height = 60
        self.__center_horz = size[0] / 2
        self.__center_vert = size[1] / 2

        self.open_menu()

    def open_menu(self):
        # get screen
        screen = pygame.display.set_mode(self.__size)
        pygame.display.set_caption("Menu")
        screen.fill((255, 255, 255))
        pygame.display.flip()

        # get ui manager
        manager = pygame_gui.UIManager(self.__size)

        # draw buttons
        start_button_text = "START"
        start_button_pos = (self.__width / 2 - self.__button_width / 2, self.__height / 2 - self.__button_height / 2 - self.__padding)
        options_button_text = "OPTIONS"
        options_button_pos = (start_button_pos[0], start_button_pos[1] + self.__button_height + self.__padding)
        quit_button_text = "QUIT"
        quit_button_pos = (options_button_pos[0], options_button_pos[1] + self.__button_height + self.__padding)

        # draw buttons
        start_button = UIButton(
            relative_rect=pygame.Rect(start_button_pos, (self.__button_width, self.__button_height)),
            manager=manager,
            text=start_button_text
                                )
        options_button = UIButton(
            relative_rect=pygame.Rect(options_button_pos, (self.__button_width, self.__button_height)),
            manager=manager,
            text=options_button_text
        )
        quit_button = UIButton(
            relative_rect=pygame.Rect(quit_button_pos, (self.__button_width, self.__button_height)),
            manager=manager,
            text=quit_button_text
        )
        manager.draw_ui(screen)

        # draw title
        title_string = "CAT GAME"
        font = pygame.font.Font(None, 32)
        text_surface = font.render(title_string, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.__width // 2, self.__height)
        screen.blit(text_surface, text_rect)


        # main loop
        running = True
        clock = pygame.time.Clock()
        while running:
            # delta time
            dt = clock.tick(60) / 1000
            manager.update(dt)

            events = pygame.event.get()
            for event in events:

                if event.type is pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()

                manager.process_events(event)
                # button events
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == start_button:
                        print("start")
                    if event.ui_element == options_button:
                        # DEBUG
                        print("options")
                    if event.ui_element == quit_button:
                        running = False
                        pygame.quit()
                        exit()


            manager.update(dt)
            manager.draw_ui(screen)

            pygame.display.update()
