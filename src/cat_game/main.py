# main file
import pygame
from Model.TerrainMap import TerrainMap
from Model.EntityMap import EntityMap
from Model.Entity.TabbyCat import TabbyCat
from Model.ENUM.EntityType import EntityType
from Model.Entity.SmallDog import SmallDog


def main():
    tm = TerrainMap("map1.txt")
    tm.debug_display()

    LOCAL_DIFF = 3
    em = EntityMap(tm, LOCAL_DIFF)

    print(em.is_in_bounds((0, 5)))
    print(em.is_walkable((0, 5)))

    # place entity
    tabby = TabbyCat()
    rand_pos = em.get_rand_valid_pos()
    em.place_entity(tabby, rand_pos)
    em.debug_display()

    small_dog = SmallDog()
    rand_pos2 = em.get_rand_valid_pos()
    em.place_entity(small_dog, rand_pos2)
    em.debug_display()
    print(rand_pos2)
    print(small_dog.get_position())



if __name__ == "__main__":
    main()
    quit()