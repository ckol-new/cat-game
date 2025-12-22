# main file
import pygame as pg
import pygame_gui as pgg
from Model.Level import Level
from Model.Roster import Roster
from Model.Entity.TabbyCat import TabbyCat
from Model.LevelMap import LevelMap


def main():
    main_entry = Main()

class Main:
    def __init__(self):
        # initialize fields
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.SCREEN_SIZE = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        # initialize pygame stuff
        pg.init()
        self.__screen = pg.display.set_mode(self.SCREEN_SIZE)

        # open menu
        self.__menu = Menu(self.__screen, self)
        self.__game = None
        self.open_menu()

    def open_menu(self):
        self.__menu.open_menu()
    def close_menu(self): ...

    def open_game(self):
        # if game is not already started, make new game
        if self.__game is None:
            self.__game = Game(self.__screen, self)

        self.__game.play_game()

class Menu:
    def __init__(self, screen, main):
        self.__screen = screen
        self.__main = main
        self.__size = (screen.get_width(), screen.get_height())
        self.__ORIGIN = (0, 0)
        self.__CENTER_HORZ = self.__size[0] / 2
        self.__CENTER_VERT = self.__size[1] /2
        self.__BUTTON_SIZE = (self.__size[0] / 10, self.__size[1] / 10)
        self.__PADDING = 20
        self.__MARGIN = 20
        self.__WHITE = (255, 255, 255)
        self.__BLACK = (0, 0, 0)

    def open_menu(self):
        # launch menu loop
        BACKGROUND = pg.Surface(self.__size)
        BACKGROUND.fill(self.__WHITE)
        self.__screen.blit(BACKGROUND)

        # get manager
        manager = pgg.UIManager(self.__size)

        # get buttons
        options_button_pos = (self.__CENTER_HORZ - (self.__BUTTON_SIZE[0] / 2), self.__CENTER_VERT - self.__BUTTON_SIZE[1] / 2)
        start_button_pos = (options_button_pos[0], options_button_pos[1] - self.__BUTTON_SIZE[1] - self.__PADDING)
        quit_button_pos = (options_button_pos[0], options_button_pos[1] + self.__BUTTON_SIZE[1] + self.__PADDING)

        start_button = pgg.elements.UIButton(
            relative_rect=pg.Rect(start_button_pos, self.__BUTTON_SIZE),
            text="START",
            manager=manager
        )
        options_button = pgg.elements.UIButton(
            relative_rect=pg.Rect(options_button_pos, self.__BUTTON_SIZE),
            text="OPTIONS",
            manager=manager
        )
        quit_button = pgg.elements.UIButton(
            relative_rect=pg.Rect(quit_button_pos, self.__BUTTON_SIZE),
            text="QUIT",
            manager=manager
        )

        # main loop
        running = True
        clock = pg.time.Clock()
        while running:
            # delta time
            dt = clock.tick(60) / 1000.0

            # event handling
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                    exit()

                manager.process_events(event)
                if event.type == pgg.UI_BUTTON_PRESSED:
                    if event.ui_element == start_button:
                        self.__main.open_game()
                    if event.ui_element == options_button:
                        #DEBUG
                        print("OPTIONS")
                    if event.ui_element == quit_button:
                        running = False
                        pg.quit()
                        exit()

            # refresh screen
            self.__screen.blit(BACKGROUND)

            # update manager
            manager.update(dt)
            manager.draw_ui(self.__screen)

            # update screen
            pg.display.update()

class Game:
    def __init__(self, screen, main):
        self.__screen = screen
        self.__main = main
        self.__size = (screen.get_width(), screen.get_height())
        self.__ORIGIN = (0, 0)
        self.__CENTER_HORZ = self.__size[0] / 2
        self.__CENTER_VERT = self.__size[1] / 2
        self.__BUTTON_SIZE = (self.__size[0] / 10, self.__size[1] / 10)
        self.__PADDING = 20
        self.__MARGIN = 20
        self.__WHITE = (255, 255, 255)
        self.__BLACK = (0, 0, 0)

        self.__continue = False # if game has already started this will be true
        self.__roster = None # if game had already started this will not be empty
        self.__level_map = None # if game had already started this will not be empty
        self.__level = None # if game had already started this will not be empty

    def play_game(self):
        # check if game has already been loaded
        if not self.__continue:
            self.__setup_game()

        self.__run_game()

    def __setup_game(self):
        self.__continue = True
        self.__roster = self.__randomize_starting_roster()
        self.__level = self.__load_level()
        self.__level_map = self.__load_level_map()

        # DEBUG
        self.__level.debug_display()

    def __run_game(self):
        # background
        BACKGROUND = pg.Surface(self.__size)
        BACKGROUND.fill(self.__WHITE)
        self.__screen.blit(BACKGROUND)

        # manager
        manager = pgg.UIManager(self.__size)

        # buttons
        menu_button_pos = self.__ORIGIN
        menu_button = pgg.elements.UIButton(
            relative_rect=pg.Rect(menu_button_pos, self.__BUTTON_SIZE),
            text="MENU",
            manager=manager
                                            )


        # main loop
        running = True
        clock = pg.time.Clock()
        while running:
            # delta time
            dt = clock.tick(60) / 1000.0
            # event handling
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                    exit()

                manager.process_events(event)
                if event.type == pgg.UI_BUTTON_PRESSED:
                    if event.ui_element == menu_button:
                        self.__main.open_menu()

            # refresh screen
            self.__screen.blit(BACKGROUND)

            # update manager
            manager.update(dt)
            manager.draw_ui(self.__screen)

            # update screen
            pg.display.update()
        ...

    # generate random starting player roster
    def __randomize_starting_roster(self, start_size=3, max_size=5):
        roster = Roster(start_size)

        for i in range(start_size):
            #TODO randomize ally types, for now just TabbyCat
            tabby_cat = TabbyCat()
            roster.add(tabby_cat)

        return roster



    # method generates level map based on difficulty
    def __load_level_map(self):
        self.__level_map = LevelMap()

    # function loads current level from level map
    def __load_level(self):
        level = Level(self.__roster)
        return level



if __name__ == "__main__":
    main()
    quit()