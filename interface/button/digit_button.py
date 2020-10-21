from .calculator_button import CalculatorButton

class DigitButton(CalculatorButton):
    
    def __init__(self, root=None, text="", command=None):
        CalculatorButton.__init__(self,
            root = root,
            text = text,
            command = command
        )