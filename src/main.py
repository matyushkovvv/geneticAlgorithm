from GeneticAlghoritm import GeneticAlghoritm
from Entity import Entity
from EntityType import EntityType
import pygame
import sys

if __name__ == '__main__':
    game = GeneticAlghoritm(200, 100)

    i = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if 3 * i < 100:
            entities = [
                Entity(i, i, EntityType.HYBRID),
                Entity(2 * i, 2 * i, EntityType.PLANT),
                Entity(3 * i, 3 * i, EntityType.PREDATOR)
            ]

            game.set_entities(entities)
            game.update_entities()

            pygame.display.flip()
            pygame.time.delay(200)  # 5 fps

            i += 1
