from tkinter import Frame
from .screen import Screen
from .keyboard.keyboard import Keyboard

class Window(Frame):

    MAX_ROW = 5
    MAX_COLUMN = 5
    WIDTH = 300
    HEIGHT = 400

    def __init__(self, root = None, title = ""):
        Frame.__init__(self, root, width=200, height=400)
        self.__root = root
        self.__set_configuration(title)
        self.__make_widgets()

    def show(self):
        """ Shows this window """
        self.__root.mainloop()

    def __set_configuration(self, title):
        self.__root.title(title)
        self.__root.geometry(f"{Window.WIDTH}x{Window.HEIGHT}")
        self.__root.resizable(False, False)
        self.__set_grid_rows_weight(1)
        self.__set_grid_columns_weight(1)

    def __set_grid_rows_weight(self, weight):
        for row in range(1, Window.MAX_ROW):
            self.__root.rowconfigure(row, weight = 1)

    def __set_grid_columns_weight(self, weight):
        for column in range(0, Window.MAX_COLUMN):
            self.__root.columnconfigure(column, weight = 1)

    def __make_widgets(self):
        screen = Screen()
        screen.grid(row=0, rowspan=1, columnspan=4)
        keyboard = Keyboard()
        keyboard.grid(row=1, rowspan=4, columnspan=4)