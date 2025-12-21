class Roster:
    def __init__(self, size, max_size=5):
        self.__roster = []
        self.__size = size
        self.__max_size = max_size

    def add(self, entity):
        if len(self.__roster) < self.__max_size:
            self.__roster.append(entity)
            return

    def remove(self, entity):
        self.__roster.remove(entity)

    def get(self, index): return self.__roster.get(index)

    def get_roster_matrix(self): return self.__roster
