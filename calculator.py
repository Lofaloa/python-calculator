from tkinter import Tk
from calculator.interface.window import Window

def main():
    window = Window(root = Tk(), title="Calculator")
    window.show()

if __name__ == "__main__":
    main()