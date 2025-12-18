from .MovementType import MovementType
from .AttackType import AttackType
from .Allegiance import Allegiance

class EntityType:
    TABBY_HEALTH = 3
    TABBY_DAMAGE = 1
    TABBY_MOVEMENT_TYPE = MovementType.ORTHOGONAL
    TABBY_MOVEMENT_RANGE = 2
    TABBY_ATTACK_TYPE = AttackType.ORTHOGONAL
    TABBY_ATTACK_RANGE = 2
    TABBY_TEXTURE = "tabby_cat.png"
    TABBY_ALLEGIANCE = Allegiance.ALLY

    SMALLDOG_HEALTH = 3
    SMALLDOG_DAMAGE = 1
    SMALLDOG_MOVEMENT_TYPE = MovementType.ORTHOGONAL
    SMALLDOG_MOVEMENT_RANGE = 2
    SMALLDOG_ATTACK_TYPE = AttackType.ORTHOGONAL
    SMALLDOG_ATTACK_RANGE = 2
    SMALLDOG_TEXTURE = "small_dog.png"
    SMALLDOG_ALLEGIANCE = Allegiance.FOE


    """
    TABBY_CAT = (3, 1, MovementType.ORTHOGONAL, 2, AttackType.ORTHOGONAL, 2, "tabby_cat.png", Allegiance.ALLY)

    def __init__(self, health, damage, movement_type, movement_range, attack_type, attack_range, texture_name, allegiance):
        self.health = health
        self.damage = damage
        self.movement_type = movement_type
        self.movement_range = movement_range
        self.attack_type = attack_type
        self.attack_range = attack_range
        self.texuture_name = texture_name
        self.allegiance = allegiance

    def get_entity_data(self):
        tuple = (self.health,
                 self.damage,
                 self.movement_type,
                 self.movement_range,
                 self.attack_type,
                 self.attack_range,
                 self.texuture_name,
                 self.allegiance)
        return tuple
    """
