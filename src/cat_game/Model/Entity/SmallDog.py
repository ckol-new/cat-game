from .Entity import Entity
from ..ENUM.EntityType import EntityType


class SmallDog(Entity):
    def __init__(self,
                 health=EntityType.SMALLDOG_HEALTH,
                 damage=EntityType.SMALLDOG_DAMAGE,
                 movement_type=EntityType.SMALLDOG_MOVEMENT_TYPE,
                 movement_range=EntityType.SMALLDOG_MOVEMENT_RANGE,
                 attack_type=EntityType.SMALLDOG_ATTACK_TYPE,
                 attack_range=EntityType.SMALLDOG_ATTACK_RANGE,
                 texture_name=EntityType.SMALLDOG_TEXTURE,
                 allegiance=EntityType.SMALLDOG_ALLEGIANCE):
        super().__init__(health, damage, movement_type, movement_range, attack_type, attack_range, texture_name, allegiance)
