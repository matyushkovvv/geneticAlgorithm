from enum import Enum


class EntityType(Enum):
    PREDATOR = 1
    HYBRID = 2
    PLANT = 3

    def get_color(self):
        color_map = {
            EntityType.PREDATOR: (255, 0, 0),
            EntityType.HYBRID: (0, 255, 0),
            EntityType.PLANT: (0, 0, 255)
        }
        return color_map[self]
