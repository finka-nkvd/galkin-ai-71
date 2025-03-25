from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Volumetric(ABC):
    @abstractmethod
    def volume(self):
        pass

class TwoDimensionalShape(Shape):
    pass

class ThreeDimensionalShape(Shape, Volumetric):
    pass

class Circle(TwoDimensionalShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(TwoDimensionalShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Rectangle(TwoDimensionalShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(TwoDimensionalShape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class Sphere(ThreeDimensionalShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 4 * math.pi * self.radius ** 2

    def perimeter(self):
        return None

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

class Cube(ThreeDimensionalShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 6 * self.side ** 2

    def perimeter(self):
        return None

    def volume(self):
        return self.side ** 3

class Cylinder(ThreeDimensionalShape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def perimeter(self):
        return None

    def volume(self):
        return math.pi * self.radius ** 2 * self.height
