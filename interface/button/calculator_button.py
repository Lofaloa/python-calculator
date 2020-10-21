from tkinter import Button

class CalculatorButton():
    
    def __init__(self, root=None, text="", command=None):
        Button.__init__(self,
            root = root,
            text = text,
            command = command
        )