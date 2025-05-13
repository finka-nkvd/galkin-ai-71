import tkinter as tk
from tkinter import ttk, colorchooser
from calculate_task1 import ShapeFactory


class ShapeDrawerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Геометрические фигуры")
        self.shape_var = tk.StringVar(value="circle")
        self.color = "red"
        self.size = tk.IntVar(value=100)
        self.current_shape = None
        self.create_widgets()
        self.update_shape()

    def create_widgets(self):
        control_frame = ttk.LabelFrame(self.root, text="Управление", padding=10)
        control_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(control_frame, text="Выберите фигуру:").grid(row=0, column=0, sticky=tk.W)
        shapes = [("Круг", "circle"), ("Квадрат", "square"), ("Треугольник", "triangle")]
        for i, (text, value) in enumerate(shapes):
            ttk.Radiobutton(
                control_frame, text=text, variable=self.shape_var,
                value=value, command=self.update_shape
            ).grid(row=0, column=i+1, sticky=tk.W, padx=5)

        ttk.Button(
            control_frame, text="Выбрать цвет",
            command=self.choose_color
        ).grid(row=1, column=0, pady=10, sticky=tk.W)

        self.color_preview = tk.Label(control_frame, bg=self.color, width=10)
        self.color_preview.grid(row=1, column=1, columnspan=3, sticky=tk.W, padx=5)

        ttk.Label(control_frame, text="Размер:").grid(row=2, column=0, sticky=tk.W)
        ttk.Scale(
            control_frame, from_=20, to=300, variable=self.size,
            command=lambda _: self.draw_shape()
        ).grid(row=2, column=1, columnspan=3, sticky=tk.EW)

        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack(padx=10, pady=10)

    def choose_color(self):
        color = colorchooser.askcolor(title="Выберите цвет")[1]
        if color:
            self.color = color
            self.color_preview.config(bg=self.color)
            self.update_shape()

    def update_shape(self):
        self.current_shape = ShapeFactory.create_shape(
            self.shape_var.get(),
            self.canvas,
            self.color
        )
        self.draw_shape()

    def draw_shape(self):
        self.canvas.delete("all")
        if self.current_shape:
            self.current_shape.draw(self.size.get())