# main file
import pygame
from Model.TerrainMap import TerrainMap
from Model.EntityMap import EntityMap
from Model.Entity.TabbyCat import TabbyCat
from Model.ENUM.EntityType import EntityType
from Model.Entity.SmallDog import SmallDog
from View.Menu import Menu


def main():
    menu = Menu()
    menu.open_menu()


if __name__ == "__main__":
    main()
    quit()