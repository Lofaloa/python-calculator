from enum import Enum

class Expression:

    class Operator(Enum):

        ADDITION = "+"
        SUBSTRACTION = "-"
        MULTIPLICATION = "*"
        DIVISION = "/"

    CHARACTERS_SET = "0123456789+-/*()."

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

    def append(self, character):
        if character == None or type(character) is not str:
            raise TypeError("Cannot write an undefined character")
        if character.isdigit():
            self.append_digit(character)
        elif character in "/-+*":
            self.append_operator(character)
        elif character == "(":
            self.open_parenthesis()
        elif character == ")":
            self.close_parenthesis()
        elif character == ".":
            self.append_dot()
        else:
            raise ValueError(f"Invalid character: {character}")

    def append_dot(self):
        ## TODO: the last dotted number should only have one dot
        if self.__is_empty() or self.__ends_with_operator():
            raise ValueError(f"Cannot append a dot to {self.__expression}")
        self.__expression += "."

    def open_parenthesis(self):
        if self.__is_empty() or self.__ends_with_operator():
            self.__expression += "("
        else:
            raise ValueError("Cannot open parenthesis")

    def __has_matching_parenthesis(self):
        count = 0
        for i in self.__expression + ")":
            if i == "(":
                count += 1
            elif i == ")":
                count -= 1
            if count < 0:
                return False
        return bool(count == 0)

    def close_parenthesis(self):
        ## check if it closing a an opening parenthesis
        if not self.__is_empty() and self.__ends_with_digit() and self.__has_matching_parenthesis():
            self.__expression += ")"
        else:
            raise ValueError("Cannot close parenthesis")

    def append_operator(self, operator):
        if type(operator) is not str:
            raise TypeError("Wrong type for the operator")
        if operator not in "*/-+":
            raise ValueError("Operator should be one of +, /, -, * but was '{operator}'")
        if self.__is_expecting_operator():
            self.__expression += operator
        else:
            raise ValueError((
                "This expression ({self.__expression}) isn't"
                "expecting an operator"
            ))

    def append_digit(self, character):
        if type(character) is not str:
            raise TypeError(f"Invalid type for the character: {character}")
        if not character.isdigit():
            raise ValueError(f"The character is not a digit: {character}")
        if int(character) < 0 or 10 < int(character):
            raise ValueError(f"Invalid digit: {character}")
        self.__expression += character

    def compute(self):
        if self.is_evaluable():
            return eval(self.__expression)
        else:
            raise ValueError(f"The expression {self.__expression} cannot be computed.")

    def clear(self):
        self.__expression = ""

    def delete_last(self):
        self.__expression = self.__expression[:-1]

    def __is_empty(self):
        return len(self.__expression) == 0

    def __ends_with_operator(self):
        return self.__expression.strip().endswith(("+", "-", "*", "/"))

    def __ends_with_digit(self):
        return not self.__is_empty() and self.__expression.strip()[-1].isdigit()

    def __is_expecting_operator(self):
        return not self.__is_empty() and not self.__ends_with_operator()