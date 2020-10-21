from .calculator_button import CalculatorButton

class DigitButton(CalculatorButton):

    BACKGROUND_COLOR = "lightgrey"

    def __init__(self, root=None, digit = "0", command = None):
        CalculatorButton.__init__(self,
            root = root,
            text = digit,
            bg = DigitButton.BACKGROUND_COLOR,
            command = command
        )