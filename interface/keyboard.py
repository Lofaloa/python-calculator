from tkinter import Frame, Button

class Keyboard(Frame):

    min_digit = 0
    max_digit = 9

    def __init__(self, root = None):
        Frame.__init__(self, root, bg="yellow", width=400, height=400)
        self.__root = root
        self.__add_digit_buttons()
        self.__add_operation_buttons()

    def digit_buttons(self):
        buttons = []
        for number in range(Keyboard.min_digit, Keyboard.max_digit + 1):
            buttons.append(Button(self.__root, text=str(number)))
        return buttons

    def __add_operation_buttons(self):
        add_button = Button(self.__root, text="+")
        minus_button = Button(self.__root, text="-")
        mul_button = Button(self.__root, text="x")
        div_button = Button(self.__root, text="÷")
        equal_button = Button(self.__root, text="=")
        dot_button = Button(self.__root, text=".")

        dot_button.grid(row=4, column=1)
        equal_button.grid(row=4, column=2)
        add_button.grid(row=4, column=3)

        div_button.grid(row=1, column=3)
        mul_button.grid(row=2, column=3)
        minus_button.grid(row=3, column=3)

    def __add_digit_buttons(self):
        digit_buttons = self.digit_buttons()

        digit_buttons[0].grid(row=4, column=0)

        digit_buttons[1].grid(row=3, column=0)
        digit_buttons[2].grid(row=3, column=1)
        digit_buttons[3].grid(row=3, column=2)

        digit_buttons[4].grid(row=2, column=0)
        digit_buttons[5].grid(row=2, column=1)
        digit_buttons[6].grid(row=2, column=2)

        digit_buttons[7].grid(row=1, column=0)
        digit_buttons[8].grid(row=1, column=1)
        digit_buttons[9].grid(row=1, column=2)