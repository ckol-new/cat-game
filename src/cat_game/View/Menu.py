import pygame
from cat_game.View.ScreenParameters import ScreenParameters

class Menu:
    def __init__(self, size=(ScreenParameters.PREF_WIDTH, ScreenParameters.PREF_HEIGHT)):
       self.__size = size

    def open_menu(self):
        # get screen
        screen = pygame.display.set_mode(self.__size)
        pygame.display.set_caption("Menu")
        pygame.display.flip()

        # main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()

            pygame.display.flip()
