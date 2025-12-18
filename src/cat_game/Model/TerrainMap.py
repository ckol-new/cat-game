from cat_game.Model.ENUM.Tile import Tile
import pathlib


class TerrainMap:
    # constructor
    def __init__(self, map_name: str):
        self.__map_name = map_name

        # get map content
        map_content = self.__get_map_file_list()

        # get map size
        self.__map_size = self.__get_map_size(map_content)

        # get terrain matrix
        self.__terrain_matrix = self.__generate_terrain_matrix(map_content)  # initialize empty

    # open map file
    def __get_map_file_list(self):
        # get map file
        path = pathlib.Path("src") / "resources" / "maps" / self.__map_name
        content = path.read_text().split("\n")
        return content

    def __get_map_size(self, content):
        str_size = content[0].split()
        int_size = []
        for char in str_size: int_size.append(int(char))
        return int_size

    # get terrain matrix from map file
    def __generate_terrain_matrix(self, content):
        # initiate terrain matrix
        t_matrix = []

        # read map file as
        i = 0 # index to append to
        for line in content:
            t_matrix.append([])
            for char in list(line):
                if (char == "."): t_matrix[i].append(Tile.STONE_FLOOR)
                elif (char == "w"): t_matrix[i].append(Tile.STONE_WALL)

            # update index
            i += 1

        return t_matrix

    def get_map_size(self): return self.__map_size
    def get_terrain_matrix(self): return self.__terrain_matrix

    # DEBUG display
    def debug_display(self):
        for row in self.__terrain_matrix:
            for tile in row:
                print(tile.getChar(), end=" ")
            print()