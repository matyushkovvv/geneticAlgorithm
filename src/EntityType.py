from enum import Enum


class EntityType(Enum):
    Predator = 1
    Hybrid = 2
    Plant = 3

    def get_color(self):
        color_map = {
            EntityType.PREDATOR: "red",
            EntityType.HYBRID: "blue",
            EntityType.PLANT: "green"
        }
        return color_map.get(self, "yeelow")        # По умолчанию желтый цвет
