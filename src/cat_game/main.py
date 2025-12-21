# main file
import pygame
from Model.TerrainMap import TerrainMap
from Model.EntityMap import EntityMap
from Model.Entity.TabbyCat import TabbyCat
from Model.ENUM.EntityType import EntityType
from Model.Entity.SmallDog import SmallDog
from Controller.MenuController import MenuController
from View.Menu import Menu

def main():
    # get menu object
    menu = go_to_menu()
    game = None

def go_to_menu():
    menu = Menu()
    return menu

def go_to_game():
    game = MenuController.start_game()

if __name__ == "__main__":
    main()
    quit()