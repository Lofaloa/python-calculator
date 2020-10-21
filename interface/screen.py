from tkinter import Tk, Frame

class Screen(Frame):

    def __init__(self, root = None):
        Frame.__init__(self, root, bg="white", width=400, height=50)
        self.__root = root