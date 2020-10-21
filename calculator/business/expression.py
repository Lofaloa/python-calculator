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

    def __is_expecting_operator(self):
        return self.__expression.strip()[-1].isdigit()

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
        pass

    def compute(self):
        if self.is_evaluable():
            return eval(self.__expression)
        else:
            raise ValueError(f"The expression {self.__expression} cannot be computed.")