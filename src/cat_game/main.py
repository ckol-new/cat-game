# main file
import pygame
from Model.TerrainMap import TerrainMap
from Model.EntityMap import EntityMap
from Model.Entity.TabbyCat import TabbyCat
from Model.ENUM.EntityType import EntityType


def main():
    tm = TerrainMap("map1.txt")
    tm.debug_display()

    LOCAL_DIFF = 3
    em = EntityMap(tm, LOCAL_DIFF)


    # place entity
    tabby = TabbyCat(EntityType.TABBY_HEALTH,
                     EntityType.TABBY_DAMAGE,
                     EntityType.TABBY_MOVEMENT_TYPE,
                     EntityType.TABBY_MOVEMENT_RANGE,
                     EntityType.TABBY_ATTACK_TYPE,
                     EntityType.TABBY_ATTACK_RANGE,
                     EntityType.TABBY_TEXTURE,
                     EntityType.TABBY_ALLEGIANCE)
    rand_pos = em.get_rand_valid_pos()
    em.place_entity(tabby, rand_pos)
    em.debug_display()

if __name__ == "__main__":
    main()
    quit()