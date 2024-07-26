from ViewDelegate import GameDelegate
from Entity import Entity
from EntityType import EntityType

if __name__ == '__main__':

    entities = [
        Entity(5, 5, EntityType.HYBRID),
        Entity(11, 56, EntityType.PLANT),
        Entity(81, 3, EntityType.PREDATOR)
    ]

    GameDelegate.init(100, 100)
    GameDelegate.draw_board()
    GameDelegate.update_entities(entities)

    GameDelegate.mainloop()
