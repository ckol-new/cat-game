from .Entity import Entity
from ..ENUM.EntityType import EntityType


class TabbyCat(Entity):
    def __init__(self,
                 health=EntityType.TABBY_HEALTH,
                 damage=EntityType.TABBY_DAMAGE,
                 movement_type=EntityType.TABBY_MOVEMENT_TYPE,
                 movement_range=EntityType.TABBY_MOVEMENT_RANGE,
                 attack_type=EntityType.TABBY_ATTACK_TYPE,
                 attack_range=EntityType.TABBY_ATTACK_RANGE,
                 texture_name=EntityType.TABBY_TEXTURE,
                 allegiance=EntityType.TABBY_ALLEGIANCE):
        super().__init__(health, damage, movement_type, movement_range, attack_type, attack_range, texture_name, allegiance)