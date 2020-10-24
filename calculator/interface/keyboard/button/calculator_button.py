from tkinter import Button
from tkinter.font import Font

class CalculatorButton(Button):

    PADDING = 5
    FONT_FAMILY = "Helvetica"
    FONT_SIZE = 24

    def __init__(self, root = None, text="", style = None, command=None):
        Button.__init__(self,
            text = text,
            cursor = "hand1",
            bg = self.__to_background_color(style),
            bd = 0,
            command = command,
            width = 300 // 4,
            font = Font(
                family = CalculatorButton.FONT_FAMILY,
                size = CalculatorButton.FONT_SIZE
            )
        )
        self.__root = root

    def __to_background_color(self, style):
        if style == "primary":
            return "#908bf0"
        elif style == "secondary" :
            return "lightblue"
        elif style == "danger" :
            return "red"
        else:
            return "lightgrey"

    def add_to_grid(self, row, column):
        self.grid(
            row = row,
            column = column,
            sticky="news",
            padx = CalculatorButton.PADDING,
            pady = CalculatorButton.PADDING
        )

    def on_click(self, command):

        def exec(callable):
            try:
                callable()
            except TypeError:
                self.__root.show_error()

        self.config(command = lambda: exec(command))
