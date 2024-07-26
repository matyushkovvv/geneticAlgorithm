import pyautogui
import pygame


class Board:
    def __init__(self, cols, rows):
        self.screen_width, self.screen_height = pyautogui.size()

        self.cols = cols
        self.rows = rows

        self.__cell_size = min(self.screen_width,
                               self.screen_height) // min(self.cols, self.rows)

        self.width = self.__cell_size * self.cols
        self.height = self.__cell_size * self.rows

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Genetic Algorithm")

        self.draw_board()

    def draw_cell(self, x, y, fill, outline="black"):
        pygame.draw.rect(self.screen, fill,
                         (x, y, self.__cell_size, self.__cell_size))
        pygame.draw.rect(self.screen, outline,
                         (x, y, self.__cell_size, self.__cell_size), 1)

    def draw_board(self):
        self.screen.fill((255, 255, 255))
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.__cell_size
                y = row * self.__cell_size
                self.draw_cell(x, y, fill="white")

    def draw_entity(self, col, row, fill):
        x = col * self.__cell_size
        y = row * self.__cell_size
        self.draw_cell(x, y, fill=fill)

    def clear_board(self):
        self.screen.fill((255, 255, 255))
        self.draw_board()

    def update_entities(self, entities_list):
        self.clear_board()

        for entity in entities_list:
            self.draw_entity(entity.x, entity.y, entity.type.get_color())
