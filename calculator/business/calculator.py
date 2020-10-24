from .expression import Expression
from .observer import Subject

class Calculator(Subject):

    def __init__(self):
        Subject.__init__(self)
        self.__expression = Expression()

    def expression(self):
        return self.__expression

    def write(self, character):
        if type(character) is not str:
            raise TypeError("Cannot write an object of type " + type(character))
        if character not in Expression.CHARACTERS_SET:
            raise TypeError("Invalid character: " + type(character))
        self.__expression.append(character)
        self.__notify()

    def delete(self):
        self.__expression.delete_last()
        self.__notify()

    def clear(self):
        self.__expression.clear()
        self.__notify()

    def result(self):
        if self.__expression.is_evaluable():
            result = str(self.__expression.compute())
            self.__expression.value(result)
            return result
        else:
            raise ValueError("Cannot get result for an incomplete expression")

    def __notify(self):
        self.notify_observers(self.__expression.value())