from tkinter import Tk, Frame, Label

class Screen(Frame):

    def __init__(self, content, root = None):
        Frame.__init__(self, root, bg="white", width=400, height=50)
        self.__root = root
        self.__label = Label(self.__root, text=content)
        self.__label.grid(row=0, rowspan=1, columnspan=4)

    def content(self, value):
        self.__label.config(text = value)