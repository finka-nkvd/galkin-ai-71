from math import factorial
from abc import ABC, abstractmethod


class CombinatoricsStrategy(ABC):
    @abstractmethod
    def calculate(self, n: int, k: int = None, with_repetitions: bool = False):
        pass


class PermutationStrategy(CombinatoricsStrategy):
    def calculate(self, n: int, k: int = None, with_repetitions: bool = False):
        if with_repetitions:
            raise ValueError("Для перестановок с повторениями нужны частоты элементов")
        return factorial(n)


class CombinationStrategy(CombinatoricsStrategy):
    def calculate(self, n: int, k: int, with_repetitions: bool = False):
        if with_repetitions:
            return factorial(n + k - 1) // (factorial(k) * factorial(n - 1))
        return factorial(n) // (factorial(k) * factorial(n - k))


class ArrangementStrategy(CombinatoricsStrategy):
    def calculate(self, n: int, k: int, with_repetitions: bool = False):
        if with_repetitions:
            return n ** k
        return factorial(n) // factorial(n - k)


class CombinatoricsCalculator:
    def __init__(self):
        self.strategies = {
            "permutations": PermutationStrategy(),
            "combinations": CombinationStrategy(),
            "arrangements": ArrangementStrategy()
        }

    def calculate(self, calc_type: str, n: int, k: int = None, with_repetitions: bool = False):
        if calc_type not in self.strategies:
            raise ValueError("Неизвестный тип расчета")

        strategy = self.strategies[calc_type]
        return strategy.calculate(n, k, with_repetitions)