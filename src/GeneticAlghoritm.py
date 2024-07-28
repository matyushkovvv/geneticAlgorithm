from ViewDelegate import ViewDelegate
from Entity import Entity, EntityType
from World import WorldType
import random


class GeneticAlghoritm:
    def __init__(self, cols, rows, world_type) -> None:
        self.__cols = cols
        self.__rows = rows

        self.rules = {}
        self.__entities_list = []
        self.__world_type = world_type
        self.gravity_entities = []

        ViewDelegate.init(cols, rows)

    def start(self):
        match self.__world_type:
            case WorldType.WATER_WORLD:
                settings_map = WorldType.WATER_WORLD.get_settings()
                self.rules = settings_map['rules']

                coordinate_pairs = set()
                for entity_name in settings_map['entity']:
                    for _ in range(settings_map['entity'][entity_name]):

                        # Добавляем сущности с уникальными координатами
                        while True:
                            x = random.randint(0, self.__cols)
                            y = random.randint(0, self.__rows)

                            if (x, y) not in coordinate_pairs:
                                coordinate_pairs.add((x, y))

                                self.__entities_list.append(
                                    Entity(x, y, EntityType[entity_name])
                                )

                                break

        for entity_name in self.rules['gravity']:
            if self.rules['gravity'][entity_name] is True:
                self.gravity_entities.append(EntityType[entity_name])

    def next_step(self):
        self.gravity_action()
        self.update_entities()

    def gravity_action(self):
        if len(self.gravity_entities) == 0:
            return

        # Найдем все сущности на которых действует гравитация
        for entity_to_move in self.__entities_list:
            if entity_to_move.type in self.gravity_entities:
                # Если ход допустимый, тогда совершаем его
                if self.acceptable_move(
                    entity_to_move.x,
                    entity_to_move.y,
                    entity_to_move.x,
                    entity_to_move.y + 1
                ):
                    self.move(
                        entity_to_move,
                        entity_to_move.x,
                        entity_to_move.y + 1
                    )

    def update_entities(self):
        ViewDelegate.update_entities(self.__entities_list)

    def move(self, entity, to_x, to_y):
        entity.x = to_x
        entity.y = to_y

    def at_entity(self, x, y):
        for entity in self.__entities_list:
            if entity.x == x and entity.y == y:
                return True

        return False

    def acceptable_move(self, from_x, from_y, to_x, to_y):
        if to_y < 0 or to_y >= self.__rows:
            return False

        if self.at_entity(to_x, to_y):
            return False

        if abs(to_x - from_x) + abs(to_y - from_y) != 1:
            return False

        return True

    def set_entities(self, entities_list):
        self.__entities_list = entities_list

    def get_entities(self):
        return self.__entities_list
