import math
class parallel:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def s(self):
        return self.a * self.b

class triang:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def s(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class circle:
    def __init__(self, radius):
        self.r = radius
    def s(self):
        return 3.14*self.r**2

class sq:
    def __init__(self, a):
        self.a = a
    def s(self):
        return self.a**2

print(parallel(3, 5).s())
print(triang(7, 5, 4).s())
print(circle(8).s())
print(sq(7).s())
