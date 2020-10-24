from tkinter import Button
from .calculator_button import CalculatorButton
from .operation import Operation

class OperationButton(CalculatorButton):

    BACKGROUND_COLOR = "lightblue"

    def __init__(self, root = None, operation = Operation.ADDITION, command = None):
        CalculatorButton.__init__(self,
            text = operation.value,
            style = "secondary",
            command = command
        )