from .Level import Level
from .Node import Node
from random import randrange

class LevelMap:
    def __init__(self, rank_size= 10, order_size= 3, max_connection = 2, difficulty=None, area=None):
        self.__STARTING_LOCAL_DIFF = 3
        self.__order_size = order_size
        self.__rank_size = rank_size
        self.__max_connection = max_connection

        self.__node_map = {}
        for r in range(self.__rank_size):
            self.__node_map[r] = []

        self.node_generator()
        self.generate_connections()
        self.sort_node_map()
        self.debug_display()


    def sort_node_map(self):
        for rank in range(self.__rank_size):
            self.__node_map.get(rank).sort(key=lambda n: n.order)

    def node_generator(self, rank_size=10, order_size=3):
        # generate each node (add to proper place)
        for rank in range(rank_size):
            if rank == 0:
                first_node = Node(rank, order_size // 2)
                self.__node_map.get(0).append(first_node)
                # self.__node_map.add(first_node)
                continue

            for order in range(order_size):
                n = Node(rank, order)
                self.__node_map.get(rank).append(n)
                # self.__node_map.add(n)

    def generate_connections(self):
        # first node connects to all
        first_node = self.__node_map.get(0)[0]
        connects_to = self.__node_map.get(1)
        first_node.add_connect_to(connects_to)

        # all subsequent nodes are randomized
        for rank in range(1, self.__rank_size):
            prev_rank = self.__node_map.get(rank - 1)
            next_rank = []
            if (rank < self.__rank_size - 1):
                next_rank = self.__node_map.get(rank + 1)

            for order in range(self.__order_size):
                current_node = self.__node_map.get(rank)[order]
                current_node_connect_from = []

                # get connections from
                for prev_node in prev_rank:
                    if current_node in prev_node.connect_to:
                        current_node_connect_from.append(prev_node)
                current_node.connect_from = current_node_connect_from

                # get future connections
                current_node_connection_to = self.__generate_connections_to(current_node)
                current_node.connect_to = current_node_connection_to

    def __generate_connections_to(self, node):
        rank = node.rank
        order = node.order

        # avoid out of bounds error
        if (rank < self.__rank_size - 1):
            connection_order = [order - 1, order, order + 1]

            # remove out of bounds order positions
            remove_order = []
            for o in connection_order:
                if o < 0 or o >= self.__order_size: remove_order.append(o)
            for o in remove_order:
                connection_order.remove(o)

            # make sure is less than max number of connections
            if len(connection_order) > self.__max_connection:
                # random number of connections
                rand_num = randrange(0, self.__max_connection + 1)

                while len(connection_order) > rand_num:
                    # random index to be removed
                    rand_index = randrange(0, len(connection_order))
                    del connection_order[rand_index]

            connections = []
            for o in connection_order:
                connections.append(self.__node_map.get(rank + 1)[o])

            return connections

    def add(self, node):
        rank = node.rank
        self.__node_map.get(rank).append(node)

    def get_rank(self, rank):
        return self.__node_map.get(rank)

    def get_node(self, rank, order):
        rank_array = self.node_generator().get(rank)
        for node in rank_array:
            if node.order == order: return node

    def debug_display(self):
        for rank in range(self.__rank_size):
            if rank == 0:
                node = self.__node_map.get(0)[0]
                print(node.to_string(), end=" ")
                print()
                continue

            for order in range(self.__order_size):
                node = self.__node_map.get(rank)[order]
                print(node.to_string(), end=" ")
            print()

