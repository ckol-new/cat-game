class Entity:
    def __init__(self, health, damage, movement_type, movement_range, attack_type, attack_range, texture_name, allegiance):
        self.__health = health
        self.__damage = damage
        self.__movement_type = movement_type
        self.__movement_range = movement_range
        self.__attack_type = attack_type
        self.__attack_range = attack_range
        self.__texture_name = texture_name
        self.__allegiance= allegiance
        self.__health = health

    # getters
    def getHealth(self): return self.__health
    def getDamage(self): return self.__damage
    def getMovementType(self): return self.__movement_type
    def getMovementRange(self): return self.__movement_range
    def getAttackType(self): return self.__attack_type
    def getAttackRange(self): return self.__attack_range
    def getTextureName(self): return self.__texture_name
    def getAllegiance(self): return self.__allegiance

    # setters
    def setHealth(self, health): self.__health = health
    def setDamage(self, damage): self.__damage = damage