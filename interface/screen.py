from tkinter import Tk, Label

class Screen(Label):

    def __init__(self, root = None, text):
        Frame.__init__(self, root, text = text)