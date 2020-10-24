from tkinter import Tk, Frame, Label, RIGHT
from tkinter.font import Font
from threading import Timer

class Screen(Frame):

    PADDING = 5
    FONT_FAMILY = "Helvetica"
    FONT_SIZE = 24

    def __init__(self, root = None, content = "", width = 0, height = 0):
        Frame.__init__(self, root, width = width, height = height)
        self.__root = root
        self.__label = Label(
            root = self.__root,
            text = content,
            bg = "white",
            borderwidth=2,
            anchor = "e",
            justify = RIGHT,
            relief="groove",
            font = Font(
                family = Screen.FONT_FAMILY,
                size = Screen.FONT_SIZE
            )
        )
        self.__label.grid(row=0, rowspan=2, columnspan=4, stick="news", padx=5, pady=5)

    def show_error(self):
        self.__label.config(bg="red")
        timer = Timer(0.5, lambda: self.__label.config(bg="white"))
        timer.start()

    def get_displayable_str(self, expression):
        expression = expression.replace("+", " + ")
        expression = expression.replace("-", " - ")
        expression = expression.replace("*", " × ")
        expression = expression.replace("/", " ÷ ")
        return expression


    def content(self, value):
        self.__label.config(text = self.get_displayable_str(value))