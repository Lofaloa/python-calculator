from tkinter import Button
from tkinter.font import Font

class CalculatorButton(Button):

    PADDING = 5
    FONT_FAMILY = "Helvetica"
    FONT_SIZE = 24

    def __init__(self, root=None, text="", command=None, bg = "white"):
        Button.__init__(self,
            root = root,
            text = text,
            cursor = "hand1",
            bg = bg,
            bd = 0,
            command = command,
            font = Font(
                family = CalculatorButton.FONT_FAMILY,
                size = CalculatorButton.FONT_SIZE
            )
        )

    def add_to_grid(self, row, column):
        self.grid(
            row = row,
            column = column,
            sticky="news",
            padx = CalculatorButton.PADDING,
            pady = CalculatorButton.PADDING
        )