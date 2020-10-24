from tkinter import Frame, Button, SOLID

from .button.digit_button import DigitButton
from .button.operation_button import OperationButton
from .button.calculator_button import CalculatorButton
from .button.result_button import ResultButton
from .button.operation import Operation

class Keyboard(Frame):

    min_digit = 0
    max_digit = 9

    def __init__(self, calculator, root = None, width = 0, height = 0):
        Frame.__init__(self, root, width = width, height = height)
        self.__root = root
        self.__calculator = calculator

        self.__add_button = CalculatorButton(self, "+", "secondary")
        self.__sub_button = CalculatorButton(self, "-", "secondary")
        self.__mul_button = CalculatorButton(self, "x", "secondary")
        self.__div_button = CalculatorButton(self, "÷", "secondary")

        self.__dot_button = CalculatorButton(self, ".", "secondary")
        self.__opening_par_button = CalculatorButton(self, "(", "secondary")
        self.__closing_par_button = CalculatorButton(self, ")", "secondary")
        self.__del_button = CalculatorButton(self, "DEL", "danger")
        self.__clear_button = CalculatorButton(self, "AC", "danger")
        self.__result_button = CalculatorButton(self, "=", "primary")

        self.__make_buttons()
        self.__add_on_click_events()

    def __make_buttons(self):
        self.__make_operation_buttons()
        self.__make_control_buttons()
        self.__make_digit_buttons()

    def __make_operation_buttons(self):
        self.__add_button.add_to_grid(row=6, column=3)
        self.__div_button.add_to_grid(row=3, column=3)
        self.__mul_button.add_to_grid(row=4, column=3)
        self.__sub_button.add_to_grid(row=5, column=3)

    def __make_control_buttons(self):
        self.__dot_button.add_to_grid(row=6, column=1)
        self.__opening_par_button.add_to_grid(row=2, column=0)
        self.__closing_par_button.add_to_grid(row=2, column=1)
        self.__del_button.add_to_grid(row=2, column=2)
        self.__clear_button.add_to_grid(row=2, column=3)
        self.__result_button.add_to_grid(row=6, column=2)

    def __make_digit_buttons(self):
        digit_buttons = self.__digit_buttons()
        dot_button = DigitButton(self.__root, digit=".")

        dot_button.add_to_grid(row=6, column=1)
        digit_buttons[0].add_to_grid(row=6, column=0)

        digit_buttons[1].add_to_grid(row=5, column=0)
        digit_buttons[2].add_to_grid(row=5, column=1)
        digit_buttons[3].add_to_grid(row=5, column=2)

        digit_buttons[4].add_to_grid(row=4, column=0)
        digit_buttons[5].add_to_grid(row=4, column=1)
        digit_buttons[6].add_to_grid(row=4, column=2)

        digit_buttons[7].add_to_grid(row=3, column=0)
        digit_buttons[8].add_to_grid(row=3, column=1)
        digit_buttons[9].add_to_grid(row=3, column=2)

    def show_error(self):
        self.__root.show_error()

    def __add_on_click_events(self):
        self.__add_button.on_click(lambda: self.__calculator.write("+"))
        self.__sub_button.on_click(lambda: self.__calculator.write("-"))
        self.__mul_button.on_click(lambda: self.__calculator.write("*"))
        self.__div_button.on_click(lambda: self.__calculator.write("/"))

        self.__opening_par_button.on_click(lambda: self.__calculator.write("("))
        self.__closing_par_button.on_click(lambda: self.__calculator.write(")"))
        self.__dot_button.on_click(lambda: self.__calculator.write("."))
        self.__dot_button.on_click(lambda: self.__calculator.write("."))

        self.__del_button.on_click(lambda: self.__calculator.delete())
        self.__clear_button.on_click(lambda: self.__calculator.clear())

    def __digit_buttons(self):
        buttons = []
        numbers = []
        for number in range(Keyboard.min_digit, Keyboard.max_digit + 1):
            buttons.append(DigitButton(self.__root,
                digit = number,
                command = lambda value = number: self.__calculator.write(str(value))
            ))
            numbers.append(number)
        return buttons