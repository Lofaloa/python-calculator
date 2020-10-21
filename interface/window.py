from tkinter import Tk, Frame
from .screen import Screen
from .keyboard import Keyboard

class Window(Frame):

    MAX_ROW = 5
    MAX_COLUMN = 4

    def __init__(self, title):
        """ Configure a grid: https://tkdocs.com/tutorial/grid.html
        """
        self.__root = Tk()

        for row in range(0, Window.MAX_ROW):
            self.__root.grid_columnconfigure(row, weight = 1)

        for column in range(0, Window.MAX_COLUMN):
            self.__root.grid_rowconfigure(column, weight = 1)

        Frame.__init__(self, self.__root)
        self.__set_configuration(title)
        self.__make_widgets()

    def __set_configuration(self, title):
        self.__root.title(title)

    def __make_widgets(self):
        screen = Screen()
        screen.grid(row=0, rowspan=1, columnspan=4)
        keyboard = Keyboard()
        keyboard.grid(row=1, rowspan=4, columnspan=4)

    def show(self):
        """ Shows this window """
        self.__root.mainloop()