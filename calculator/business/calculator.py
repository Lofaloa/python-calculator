from .expression import Expression
from .observer import Subject

class Calculator(Subject):

    def __init__(self):
        Subject.__init__(self)
        self.__expression = ""

    def expression(self):
        return self.__expression

    def write(self, character):
        self.__expression += str(character)
        self.notify_observers(self.__expression)

    # def result(self):
    #     if self.__expression.is_evaluable():
    #         return self.__expression.compute()
    #     else:
    #         raise ValueError("Cannot get result for an incomplete expression")