from enum import Enum


class EntityType(Enum):
    PREDATOR = 1
    HYBRID = 2
    HERBIVORES = 3
    PLANT = 4
    MINERAL = 5

    def get_color(self):
        color_map = {
            EntityType.PREDATOR: (255, 0, 0),
            EntityType.HYBRID: (0, 255, 0),
            EntityType.HERBIVORES: (255, 130, 130),
            EntityType.PLANT: (0, 0, 255),
            EntityType.MINERAL: (194, 232, 90)
        }
        return color_map[self]


class Entity:
    def __init__(self, x_cord, y_cord, type) -> None:
        self.x = x_cord
        self.y = y_cord

        self.type = type
