from enum import Enum

class Tile(Enum):
    STONE_FLOOR = (True, "stone_floor.png", ".")
    STONE_WALL = (False, "stone_wall.png", "w")

    # constructor
    def __init__(self, walkable, texture_name, char):
        self.__walkable = walkable
        self.__texture_name = texture_name
        self.__char = char

    # getters
    def isWalkable(self):
        return self.__walkable
    def getTextureName(self):
        return self.__texture_name
    def getChar(self): return self.__char