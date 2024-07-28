from BoardView import Board


class ViewDelegate:
    @staticmethod
    def init(cols, rows):
        ViewDelegate.board = Board(cols, rows)

    @staticmethod
    def update_entities(entities_list):
        ViewDelegate.board.update_entities(entities_list)
