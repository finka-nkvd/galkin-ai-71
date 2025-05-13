from abc import ABC, abstractmethod
from itertools import permutations, combinations, product

class CombinatoricsCalculator(ABC):
    @abstractmethod
    def calculate(self, n, k=None):
        pass

class PermutationCalculator(CombinatoricsCalculator):
    def calculate(self, n, k=None):
        return list(permutations(range(n)))

class CombinationCalculator(CombinatoricsCalculator):
    def calculate(self, n, k):
        return list(combinations(range(n), k))

class ArrangementCalculator(CombinatoricsCalculator):
    def calculate(self, n, k):
        return list(product(range(n), repeat=k))

class CalculatorFactory:
    @staticmethod
    def create_calculator(calculation_type):
        calculators = {
            "permutations": PermutationCalculator,
            "combinations": CombinationCalculator,
            "arrangements": ArrangementCalculator
        }
        return calculators[calculation_type]()

class CircleVisualizer:
    def __init__(self, colors):
        self.colors = colors

    def draw_combination(self, combination, canvas):
        canvas.delete("all")
        for i, item in enumerate(combination):
            x = 100 + (i % 5) * 120
            y = 100 + (i // 5) * 120
            canvas.create_oval(x, y, x + 80, y + 80,
                             fill=self.colors[item], outline='black')