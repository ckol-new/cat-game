from .Entity.Entity import Entity
from .Entity.TabbyCat import TabbyCat
from .Entity.SmallDog import SmallDog
from .TerrainMap import TerrainMap
import random as rand

class EntityMap:
    def __init__(self, terrain_map):
        self.__PASSABLE = None # None represents passable
        self.__IMPASSABLE = 1 # 1 represents impassable
        self.__map_size = terrain_map.get_map_size()

        # convert terrain matrix to entity matrix
        self.__entity_matrix = self.__convert_to_entity_matrix(terrain_map.get_terrain_matrix())

        # active entity array
        self.__active_entity_array = []


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

    # move entity
    def move_entity(self, entity, new_pos):
        if not self.is_in_bounds(new_pos): raise Exception("TRIED TO MOVE ENTITY OFF OF THE GRID")
        if not self.is_walkable(new_pos): raise Exception("TRIED TO MOVE ENTITY ONTO UNWALKABLE POSITION")

        old_pos = entity.get_position()
        self.__entity_matrix[new_pos[0]][new_pos[1]] = entity
        self.__entity_matrix[old_pos[0]][old_pos[1]] = self.__PASSABLE
        entity.set_position(new_pos)

    # kill entity (remove from entity matrix and active entity array)
    # returns void
    def kill_entity(self, entity):
        pos = entity.get_position()
        self.__entity_matrix[pos[0]][pos[1]] = self.__PASSABLE
        self.__active_entity_array.remove(entity)

    # def entity is alive (in active entity array list, and has health greater than 0
    # return boolean
    def is_alive(self, entity):
        if entity.get_health() <= 0: return False
        elif not (entity in self.__active_entity_array): return False

        return True


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
        entity.set_position(position)
        self.__active_entity_array.append(entity)


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
                elif e == self.__IMPASSABLE: print("w", end=" ")
                elif type(e) is TabbyCat: print("T", end=" ")
                elif type(e) is SmallDog: print("S", end=" ")
            print()