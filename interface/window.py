from tkinter import Tk, Frame

class Window(Frame):

    def __init__(self, title):
        self.__root = Tk()
        Frame.__init__(self, self.__root)
        self.__set_configuration(title)

    def __set_configuration(self, title):
        self.__root.title(title)

    def __make_widgets(self):
        pass

    def show(self):
        """ Shows this window """
        self.__root.mainloop()