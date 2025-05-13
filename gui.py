import tkinter as tk
from logic import Calculator


class CalculatorGUI:
    def __init__(self, root):
        self.calculator = Calculator()
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry('400x100')

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text='=', command=self.on_calculate)
        self.button.pack()

        self.ans_label = tk.Label(root, text='')
        self.ans_label.pack(pady=10)

    def on_calculate(self):
        expression = self.entry.get()
        try:
            result = self.calculator.calculate(expression)
            self.ans_label.config(text=str(result))
        except ValueError as e:
            self.ans_label.config(text=str(e))

root = tk.Tk()
app = CalculatorGUI(root)
root.mainloop()
