import tkinter as tk
import pyautogui


class Board:
    def __init__(self, cols, rows):
        self.screen_width, self.screen_height = pyautogui.size()

        self.cols = cols
        self.rows = rows

        self.__cell_size = min(self.screen_width,
                               self.screen_height) // min(cols, rows)

        self.root = tk.Tk()
        self.root.title("Genetic Algorithm")

        self.canvas = tk.Canvas(
            self.root,
            width=self.cols * self.__cell_size,
            height=self.rows * self.__cell_size
        )

        self.canvas.pack()
        self.draw_board()

        self.update_board()

    def draw_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * self.__cell_size
                y1 = row * self.__cell_size
                x2 = x1 + self.__cell_size
                y2 = y1 + self.__cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")

    def draw_entities(self, entities_list):
        for entity in entities_list:
            x1 = entity.col * self.__cell_size
            y1 = entity.row * self.__cell_size
            x2 = x1 + self.__cell_size
            y2 = y1 + self.__cell_size
            self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")

    def update_board(self):
        self.canvas.delete("entity")

        self.draw_entities()

        self.root.after(200, self.update_board)     # 5 fps

    def mainloop(self):
        self.root.mainloop()
