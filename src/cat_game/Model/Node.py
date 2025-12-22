class Node:
    def __init__(self, rank, order):
        self.rank = rank
        self.order = order

        self.connect_to = None
        self.connect_from = None

        self.__event = None

    def add_connect_to(self, connection): self.connect_to = connection
    def add_connect_from(self, connection): self.connect_from = connection
    def add_event(self, event): self.event = event

    def to_string(self): return f"({self.rank}, {self.order})"

    def get_evenet(self): return self.event

