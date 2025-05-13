import tkinter as tk
from tkinter import ttk
from calculate_task3 import CalculatorFactory, CircleVisualizer


class CombinatoricsVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Визуализатор комбинаторики")
        self.visualizer = CircleVisualizer(['red', 'green', 'blue',
                                            'yellow', 'purple', 'orange'])
        self.current_combination = 0
        self.combinations = []
        self.setup_ui()

    def setup_ui(self):
        self.setup_controls()
        self.setup_canvas()
        self.setup_navigation()

    def setup_controls(self):
        control_frame = ttk.Frame(self.root)
        control_frame.pack(pady=10)

        self.calculation_type = tk.StringVar(value="permutations")

        ttk.Radiobutton(control_frame, text="Перестановки",
                        variable=self.calculation_type, value="permutations",
                        command=self.update_calculation).grid(row=0, column=0)

        ttk.Radiobutton(control_frame, text="Сочетания",
                        variable=self.calculation_type, value="combinations",
                        command=self.update_calculation).grid(row=0, column=1)

        ttk.Radiobutton(control_frame, text="Размещения",
                        variable=self.calculation_type, value="arrangements",
                        command=self.update_calculation).grid(row=0, column=2)

        ttk.Label(control_frame, text="Всего элементов (n):").grid(row=1, column=0)
        self.n_var = tk.IntVar(value=3)
        ttk.Spinbox(control_frame, from_=1, to=6, textvariable=self.n_var,
                    command=self.update_calculation).grid(row=1, column=1)

        self.k_label = ttk.Label(control_frame, text="Выбираемых элементов (k):")
        self.k_var = tk.IntVar(value=2)
        self.k_spin = ttk.Spinbox(control_frame, from_=1, to=6,
                                  textvariable=self.k_var,
                                  command=self.update_calculation)

    def setup_canvas(self):
        self.canvas = tk.Canvas(self.root, width=700, height=400, bg='white')
        self.canvas.pack(pady=10)

    def setup_navigation(self):
        nav_frame = ttk.Frame(self.root)
        nav_frame.pack()

        ttk.Button(nav_frame, text="Назад",
                   command=self.show_previous).pack(side=tk.LEFT)

        ttk.Button(nav_frame, text="Вперед",
                   command=self.show_next).pack(side=tk.LEFT)

        self.status_label = ttk.Label(nav_frame, text="")
        self.status_label.pack(side=tk.LEFT, padx=10)

    def update_calculation(self):
        calculator = CalculatorFactory.create_calculator(self.calculation_type.get())
        n = self.n_var.get()

        if self.calculation_type.get() == "permutations":
            self.combinations = calculator.calculate(n)
            self.k_label.grid_remove()
            self.k_spin.grid_remove()
        else:
            k = self.k_var.get()
            self.combinations = calculator.calculate(n, k)
            self.k_label.grid(row=1, column=2)
            self.k_spin.grid(row=1, column=3)

        self.current_combination = 0
        self.update_display()

    def update_display(self):
        if self.combinations:
            self.visualizer.draw_combination(
                self.combinations[self.current_combination],
                self.canvas
            )
            self.status_label.config(
                text=f"Комбинация {self.current_combination + 1} из {len(self.combinations)}"
            )
        else:
            self.canvas.delete("all")
            self.status_label.config(text="Нет комбинаций")

    def show_next(self):
        if self.combinations:
            self.current_combination = (self.current_combination + 1) % len(self.combinations)
            self.update_display()

    def show_previous(self):
        if self.combinations:
            self.current_combination = (self.current_combination - 1) % len(self.combinations)
            self.update_display()