from tkinter import Button
from .calculator_button import CalculatorButton

class OperationButton(CalculatorButton):
    
    def __init__(self, root=None, text="", command=None):
        CalculatorButton.__init__(self,
            root = root,
            text = text,
            command = command
        )