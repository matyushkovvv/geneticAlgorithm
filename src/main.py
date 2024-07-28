from GeneticAlghoritm import GeneticAlghoritm
from World import WorldType
import pygame
import sys

if __name__ == '__main__':

    game = GeneticAlghoritm(70, 70, WorldType.WATER_WORLD)
    game.start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.next_step()

        pygame.display.flip()
        pygame.time.delay(200)  # 5 fps
