from cat_game.View.Game import Game


class MenuController:
    def start_game(self):
        game = Game()
        game.open_game()
        return game