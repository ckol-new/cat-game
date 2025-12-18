class Entity:
    def __init__(self, health, damage, movement_type, movement_range, attack_type, attack_range, texture_name, allegiance, position=(-1, -1)):
        self.__health = health
        self.__damage = damage
        self.__movement_type = movement_type
        self.__movement_range = movement_range
        self.__attack_type = attack_type
        self.__attack_range = attack_range
        self.__texture_name = texture_name
        self.__allegiance= allegiance
        self.__health = health
        self.__position = position



    # getters
    def get_health(self): return self.__health
    def get_damage(self): return self.__damage
    def get_movement_type(self): return self.__movement_type
    def get_movement_range(self): return self.__movement_range
    def get_attack_type(self): return self.__attack_type
    def get_attack_range(self): return self.__attack_range
    def get_texture_name(self): return self.__texture_name
    def get_allegiance(self): return self.__allegiance
    def get_position(self): return self.__position

    # setters
    def set_health(self, health): self.__health = health
    def set_damage(self, damage): self.__damage = damage
    def set_position(self, new_position): self.__position = new_position