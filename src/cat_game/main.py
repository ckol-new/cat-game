# main file
import pygame
from Model.TerrainMap import TerrainMap


def main():
    tm = TerrainMap("map2.txt")
    tm.debug_display()


if __name__ == "__main__":
    main()
    quit()