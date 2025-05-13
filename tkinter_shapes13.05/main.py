import tkinter as tk
from tkinter import ttk
from gui_task1 import ShapeDrawerApp
from gui_task2 import CombinatoricsUI
from gui_task3 import CombinatoricsVisualizer

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Главное меню")
        self.root.geometry('250x150')
        self.create_widgets()

    def create_widgets(self):
        ttk.Button(self.root, text="Геометрические фигуры",
                  command=self.open_task1).pack(pady=10)
        ttk.Button(self.root, text="Калькулятор комбинаторики",
                  command=self.open_task2).pack(pady=10)
        ttk.Button(self.root, text="Визуализатор комбинаторики",
                  command=self.open_task3).pack(pady=10)

    def open_task1(self):
        window = tk.Toplevel(self.root)
        ShapeDrawerApp(window)

    def open_task2(self):
        window = tk.Toplevel(self.root)
        CombinatoricsUI(window)

    def open_task3(self):
        window = tk.Toplevel(self.root)
        CombinatoricsVisualizer(window)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()