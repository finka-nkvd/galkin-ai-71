import tkinter as tk
from tkinter import ttk
from calculate_task2 import CombinatoricsCalculator


class CombinatoricsUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор комбинаторики")
        self.calculator = CombinatoricsCalculator()
        self.create_variables()
        self.create_widgets()

    def create_variables(self):
        self.calculation_type = tk.StringVar(value="permutations")
        self.with_repetitions = tk.BooleanVar(value=False)
        self.n = tk.StringVar()
        self.k = tk.StringVar()
        self.result = tk.StringVar(value="Результат: ")

    def create_widgets(self):
        self.create_type_frame()
        self.create_param_frame()
        self.create_action_frame()
        self.update_ui()

    def create_type_frame(self):
        type_frame = ttk.LabelFrame(self.root, text="Тип расчета", padding=10)
        type_frame.pack(padx=10, pady=5, fill=tk.X)

        types = [
            ("Перестановки", "permutations"),
            ("Сочетания", "combinations"),
            ("Размещения", "arrangements")
        ]

        for text, value in types:
            ttk.Radiobutton(
                type_frame, text=text, variable=self.calculation_type,
                value=value, command=self.update_ui
            ).pack(side=tk.LEFT, padx=5)

    def create_param_frame(self):
        param_frame = ttk.LabelFrame(self.root, text="Параметры", padding=10)
        param_frame.pack(padx=10, pady=5, fill=tk.X)

        ttk.Checkbutton(
            param_frame, text="С повторениями",
            variable=self.with_repetitions
        ).pack(anchor=tk.W)

        ttk.Label(param_frame, text="n (общее количество элементов):").pack(anchor=tk.W)
        ttk.Entry(param_frame, textvariable=self.n).pack(fill=tk.X)

        self.k_label = ttk.Label(param_frame, text="k (выбираемое количество элементов):")
        self.k_entry = ttk.Entry(param_frame, textvariable=self.k)

    def create_action_frame(self):
        action_frame = ttk.Frame(self.root, padding=10)
        action_frame.pack(padx=10, pady=5, fill=tk.X)

        ttk.Button(
            action_frame, text="Рассчитать",
            command=self.perform_calculation
        ).pack(side=tk.LEFT)

        ttk.Label(
            action_frame, textvariable=self.result,
            font=('Helvetica', 10, 'bold')
        ).pack(side=tk.LEFT, padx=10)

    def update_ui(self):
        if self.calculation_type.get() == "permutations":
            self.k_label.pack_forget()
            self.k_entry.pack_forget()
        else:
            self.k_label.pack(anchor=tk.W)
            self.k_entry.pack(fill=tk.X)

    def perform_calculation(self):
        try:
            n = int(self.n.get())
            if n <= 0:
                raise ValueError("n должно быть положительным числом")

            calc_type = self.calculation_type.get()
            with_rep = self.with_repetitions.get()
            k = int(self.k.get()) if calc_type != "permutations" else None

            if calc_type != "permutations" and (k <= 0 or k > n):
                raise ValueError("k должно быть положительным и не больше n")

            result = self.calculator.calculate(calc_type, n, k, with_rep)
            self.result.set(f"Результат: {result}")

        except ValueError as e:
            self.result.set(f"Ошибка: {str(e)}")
