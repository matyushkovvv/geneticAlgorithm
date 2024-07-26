from BoardView import Board


class Delegate:
    @staticmethod
    def init(cols, rows):
        Delegate.board = Board(cols, rows)

    @staticmethod
    def update_entities(entities_list):
        Delegate.board.update_entities(entities_list)
