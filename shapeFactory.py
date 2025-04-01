import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def get_type(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def get_type(self):
        return "Круг"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def get_type(self):
        return "Квадрат"


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def get_type(self):
        return "Треугольник"


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == "circle":
            return Circle(*args)
        elif shape_type == "square":
            return Square(*args)
        elif shape_type == "triangle":
            return Triangle(*args)
        else:
            raise ValueError("Недопустимый тип фигуры")


def main():
    while True:
        print("\nМеню создания фигур:")
        print("1. Круг")
        print("2. Квадрат")
        print("3. Треугольник")
        print("4. Выход")

        choice = input("Выберите тип фигуры (или введите тип вручную): ")

        if choice == "1" or choice == "circle":
            radius = float(input("Введите радиус круга: "))
            shape = ShapeFactory.create_shape("circle", radius)
        elif choice == "2" or choice == "square":
            side = float(input("Введите сторону квадрата: "))
            shape = ShapeFactory.create_shape("square", side)
        elif choice == "3" or choice == "triangle":
            base = float(input("Введите основание треугольника: "))
            height = float(input("Введите высоту треугольника: "))
            shape = ShapeFactory.create_shape("triangle", base, height)
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Недопустимый выбор. Пожалуйста, выберите действие из меню.")
            continue

        print(f"\nТип фигуры: {shape.get_type()}")
        print(f"Площадь фигуры: {shape.area():.2f}")


 main()
