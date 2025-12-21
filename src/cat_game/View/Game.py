import pygame

from cat_game.View.ScreenParameters import ScreenParameters


class Game:
    def __init__(self, difficulty=None, save_file=None):
        self.difficulty = difficulty
        self.save_file = save_file
        self.WHITE = (255, 255, 255)
        self.BLACK = (0,0,0)
        pygame.init()

    def open_game(self):
        # get screen
        size = (ScreenParameters.PREF_WIDTH, ScreenParameters.PREF_HEIGHT)
        screen = pygame.display.setmode(size)
        screen.fill(self.WHITE)
        pygame.display.set_caption("Game")
        pygame.display.flip()

        # main loop
        running = True
        while running:
            # event handling
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()


            pygame.display.flip()