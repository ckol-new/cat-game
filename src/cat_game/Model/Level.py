from multiprocessing.forkserver import connect_to_new_process

from .TerrainMap import TerrainMap
from .EntityMap import EntityMap
from .Entity.SmallDog import SmallDog

class Level:
    def __init__(self, roster, area=None, local_difficulty=3, connecting_from=None, connecting_to=None):
        self.__area = area
        self.__local_diff = local_difficulty
        self.__ally_roster = roster

        self.__terrain_map = self.__load_terrain()
        self.__entity_map = self.__load_entity_map()
        self.__enemy_roster = self.__generate_enemy_roster()
        self.__randomize_enemy_position()

        self.__randomize_ally_position()

        # connections
        self.__connecting_from = connecting_from
        self.__connecting_to = connecting_to

        #TODO implement player choosing wear allies go, randomize rewards, etc.


    # load terrain based on area
    def __load_terrain(self):
        #DEBUG just use map1
        map_name = "map1.txt"

        # build terrain map
        tm = TerrainMap(map_name)
        return tm


    # randomize map
    def __random_map(self): ...

    # load entity map
    def __load_entity_map(self):
        em = EntityMap(self.__terrain_map)
        return em


    # randomize player position
    def __randomize_ally_position(self):
        for ally in self.__ally_roster.get_roster_matrix():
            rand_pos = self.__entity_map.get_rand_valid_pos()
            self.__entity_map.place_entity(ally, rand_pos)


    # get enemy roster (based on local difficulty
    def __generate_enemy_roster(self):
        er = []
        enemy_cost = {type(SmallDog): 1, }

        if self.__local_diff < 7:
            points = self.__local_diff
        else: points = 7
        while points > 0:
            # get rand enemy
            #TODO randomize enemy

            # DEBUG just use small dog
            sm = SmallDog()
            er.append(sm)
            points = points - 1

        return er

    # randomize enemy position
    def __randomize_enemy_position(self):
        for enemy in self.__enemy_roster:
            rand_pos = self.__entity_map.get_rand_valid_pos()
            self.__entity_map.place_entity(enemy, rand_pos)



    # randomize player reward options (based on local_difficulty and area)
    def __randomize_reward_options(self):
        ...

    # add connecting from
    def add_connection_from(self, connecting_from): self.__connecting_from = connecting_from
    def add_connection_to(self, connecting_to): self.__connecting_to = connecting_to

    #DEBUG
    def debug_display(self):
        self.__terrain_map.debug_display()
        print()
        self.__entity_map.debug_display()
