from tkinter import Tk, Frame
from .screen import Screen
from .keyboard import Keyboard

class Window(Frame):

    def __init__(self, title):
        self.__root = Tk()
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