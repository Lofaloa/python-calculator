from enum import Enum

class Expression:

    class Operator(Enum):

        ADDITION = "+"
        SUBSTRACTION = "-"
        MULTIPLICATION = "*"
        DIVISION = "/"

    def __init__(self, expression = ""):
        self.__expression = expression

    def is_evaluable(self):
        try:
            eval(self.__expression)
            return True
        except:
            return False

    def value(self):
        return self.__expression

    def append_operator(self, operator):
        if type(operator) is not Expression.Operator:
            raise TypeError("Wrong type for the operator")
        if self.__is_expecting_operator():
            self.__expression += f" {operator.value}"
        else:
            raise ValueError((
                "This expression ({self.__expression}) isn't"
                "expecting an operator"
            ))

    def append_digit(self, digit):
        if type(digit) is not int:
            raise TypeError(f"Invalid type for the digit: {digit}")
        if digit < 0 or 10 < digit:
            raise ValueError(f"Invalid digit: {digit}")
        if self.__ends_with_digit():
            self.__expression += str(digit)
        else:
            self.__expression += f" {digit}"

    def compute(self):
        if self.is_evaluable():
            return eval(self.__expression)
        else:
            raise ValueError(f"The expression {self.__expression} cannot be computed.")

    def __is_empty(self):
        return len(self.__expression) == 0

    def __ends_with_operator(self):
        return self.__expression.strip().endswith(("+", "-", "*", "/"))

    def __ends_with_digit(self):
        return not self.__is_empty() and self.__expression.strip()[-1].isdigit()

    def __is_expecting_operator(self):
        return not self.__is_empty() and not self.__ends_with_operator()