from .Entity.Entity import Entity
from .Entity.TabbyCat import TabbyCat
from .TerrainMap import TerrainMap
import random as rand

class EntityMap:
    def __init__(self, terrain_map, local_difficulty):
        self.__local_difficulty = local_difficulty
        self.__PASSABLE = None # None represents passable
        self.__IMPASSABLE = 1 # 1 represents impassable
        self.__map_size = terrain_map.get_map_size()

        # convert terrain matrix to entity matrix
        self.__entity_matrix = self.__convert_to_entity_matrix(terrain_map.get_terrain_matrix())


    # convert to entity map
    def __convert_to_entity_matrix(self, terrain_matrix):
        e_matrix = []
        i = 0
        for row in terrain_matrix:
            e_matrix.append([])

            for tile in row:
                if tile.isWalkable():
                    e_matrix[i].append(self.__PASSABLE)
                else:
                    e_matrix[i].append(self.__IMPASSABLE)

            i += 1

        return e_matrix

    # randomize valid pos
    def get_rand_valid_pos(self):
        is_valid = False
        rand_pos = []
        while not is_valid:
            rand_pos = [rand.randrange(0, self.__map_size[0]), rand.randrange(0, self.__map_size[1])]
            if self.is_walkable(rand_pos):
                is_valid = True

        return rand_pos

    # place entity at given position
    def place_entity(self, entity, position):
        if not self.is_walkable(position):
            raise Exception("POSITION IS NOT WALKABLE")
        self.__entity_matrix[position[0]][position[1]] = entity


    # is in bound
    def is_in_bounds(self, pos):
        if (pos[0] < 0 or pos[0] >= self.__map_size[0]) or (pos[1] < 0 or pos[1] >= self.__map_size[1]):
            return False
        return True

    # is walkable position
    def is_walkable(self, pos):
        if not self.is_in_bounds(pos): return False

        if self.__entity_matrix[pos[0]][pos[1]] == self.__PASSABLE:
            return True
        else: return False

    def get_map_size(self): return self.__map_size

    # DEBUG display
    def debug_display(self):
        for row in self.__entity_matrix:
            for e in row:
                if e == self.__PASSABLE: print(".", end=" ")
                if e == self.__IMPASSABLE: print("w", end=" ")
                if type(e) == TabbyCat: print("T", end=" ")
            print()