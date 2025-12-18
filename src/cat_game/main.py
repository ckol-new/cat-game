# main file
import pygame
from Model.TerrainMap import TerrainMap
from Model.EntityMap import EntityMap


def main():
    tm = TerrainMap("map1.txt")
    tm.debug_display()

    LOCAL_DIFF = 3
    em = EntityMap(tm, LOCAL_DIFF)
    em.debug_display()

if __name__ == "__main__":
    main()
    quit()