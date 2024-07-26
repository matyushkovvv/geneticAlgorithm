from enum import Enum


class EntityType(Enum):
    PREDATOR = 1
    HYBRID = 2
    PLANT = 3

    def get_color(self):
        color_map = {
            EntityType.PREDATOR: "red",
            EntityType.HYBRID: "blue",
            EntityType.PLANT: "green"
        }
        return color_map.get(self, "yellow")        # По умолчанию желтый цвет
