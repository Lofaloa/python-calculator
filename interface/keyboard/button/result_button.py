from tkinter import Button
from .calculator_button import CalculatorButton
from .operation import Operation

class ResultButton(CalculatorButton):

    def __init__(self, root=None, command=None):
        CalculatorButton.__init__(self,
            root = root,
            text = "=",
            bg = "#908bf0",
            command = command
        )