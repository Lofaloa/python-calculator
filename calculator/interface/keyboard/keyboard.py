from tkinter import Frame, Button

from .button.digit_button import DigitButton
from .button.operation_button import OperationButton
from .button.calculator_button import CalculatorButton
from .button.result_button import ResultButton
from .button.operation import Operation

class Keyboard(Frame):

    min_digit = 0
    max_digit = 9

    def __init__(self, calculator, root = None):
        Frame.__init__(self, root, bg="white", width=400, height=400)
        self.__root = root
        self.__add_button = OperationButton(root, Operation.ADDITION)
        self.__sub_button = OperationButton(root, Operation.SUBSTRACTION)
        self.__mul_button = OperationButton(root, Operation.MULTIPLICATION)
        self.__div_button = OperationButton(root, Operation.DIVISION)

        self.__calculator = calculator

        self.__add_result_button()
        self.__make_digit_buttons()
        self.__make_operation_buttons()

    def __add_result_button(self):
        result_button = ResultButton(self.__root)
        result_button.add_to_grid(row = 4, column = 2)

    def __make_operation_buttons(self):
        self.__add_button.add_to_grid(row=4, column=3)
        self.__div_button.add_to_grid(row=1, column=3)
        self.__mul_button.add_to_grid(row=2, column=3)
        self.__sub_button.add_to_grid(row=3, column=3)
        self.__add_on_click_events()

    def __digit_buttons(self):
        buttons = []
        numbers = []
        for number in range(Keyboard.min_digit, Keyboard.max_digit + 1):
            buttons.append(DigitButton(self.__root,
                digit = number,
                command = lambda value = number: self.__calculator.write(value)
            ))
            numbers.append(number)
        print(numbers)
        return buttons

    def __make_digit_buttons(self):
        digit_buttons = self.__digit_buttons()
        dot_button = DigitButton(self.__root, digit=".")

        dot_button.add_to_grid(row=4, column=1)
        digit_buttons[0].add_to_grid(row=4, column=0)

        digit_buttons[1].add_to_grid(row=3, column=0)
        digit_buttons[2].add_to_grid(row=3, column=1)
        digit_buttons[3].add_to_grid(row=3, column=2)

        digit_buttons[4].add_to_grid(row=2, column=0)
        digit_buttons[5].add_to_grid(row=2, column=1)
        digit_buttons[6].add_to_grid(row=2, column=2)

        digit_buttons[7].add_to_grid(row=1, column=0)
        digit_buttons[8].add_to_grid(row=1, column=1)
        digit_buttons[9].add_to_grid(row=1, column=2)

    def __add_on_click_events(self):
        self.__add_button.on_click(lambda: self.__calculator.write("+"))
        self.__sub_button.on_click(lambda: self.__calculator.write("-"))
        self.__mul_button.on_click(lambda: self.__calculator.write("x"))
        self.__div_button.on_click(lambda: self.__calculator.write("/"))