from EntityType import EntityType


class Entity:
    def __init__(self, x_cord, y_cord, type: EntityType) -> None:
        self.x = x_cord
        self.y = y_cord

        self.type = type.value
