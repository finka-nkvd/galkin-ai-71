from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color

    @abstractmethod
    def draw(self, size):
        pass

class Circle(Shape):
    def draw(self, size):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        self.canvas.create_oval(
            canvas_width / 2 - size / 2,
            canvas_height / 2 - size / 2,
            canvas_width / 2 + size / 2,
            canvas_height / 2 + size / 2,
            fill=self.color, outline="black"
        )

class Square(Shape):
    def draw(self, size):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        self.canvas.create_rectangle(
            canvas_width / 2 - size / 2,
            canvas_height / 2 - size / 2,
            canvas_width / 2 + size / 2,
            canvas_height / 2 + size / 2,
            fill=self.color, outline="black"
        )

class Triangle(Shape):
    def draw(self, size):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        self.canvas.create_polygon(
            canvas_width / 2, canvas_height / 2 - size / 2,
            canvas_width / 2 - size / 2, canvas_height / 2 + size / 2,
            canvas_width / 2 + size / 2, canvas_height / 2 + size / 2,
            fill=self.color, outline="black"
        )

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, canvas, color):
        shapes = {
            "circle": Circle,
            "square": Square,
            "triangle": Triangle
        }
        return shapes[shape_type](canvas, color)