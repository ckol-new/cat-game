from .Entity import Entity

class TabbyCat(Entity):
    def __init__(self, health, damage, movement_type, movement_range, attack_type, attack_range, texture_name, allegiance):
        super().__init__(health, damage, movement_type, movement_range, attack_type, attack_range, texture_name, allegiance)