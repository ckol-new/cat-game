from .Entity.Entity import Entity
from .Entity.TabbyCat import TabbyCat
from .TerrainMap import TerrainMap

class EntityMap:
    def __init__(self, terrain_map, local_difficulty):
        self.__local_difficulty = local_difficulty
        self.__PASSABLE = 0 # 0 represents passable
        self.__IMPASSABLE = 1 # 1 represents impassable
        self__map_size = terrain_map.get_map_size()

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

    # DEBUG display
    def debug_display(self):
        for row in self.__entity_matrix:
            for e in row:
                if e == self.__PASSABLE: print(".", end=" ")
                if e == self.__IMPASSABLE: print("w", end=" ")
            print()