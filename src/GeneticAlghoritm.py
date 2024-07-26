from ViewDelegate import Delegate


class GeneticAlghoritm:
    def __init__(self, cols, rows, entities_list=[]) -> None:
        self.__entities_list = entities_list
        Delegate.init(cols, rows)

    def update_entities(self):
        Delegate.update_entities(self.__entities_list)

    def set_entities(self, entities_list):
        self.__entities_list = entities_list

    def get_entities(self):
        return self.__entities_list
