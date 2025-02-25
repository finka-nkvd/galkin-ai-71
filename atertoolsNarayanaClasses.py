import itertools


class Combinator:
    def __init__(self, elements):
        self.elements = elements

    def narayana(self):
        n = len(self.elements)
        result = []

        def generate_combination(prefix, remaining):
            if len(prefix) == n:
                result.append(prefix)
                return
            for i in range(len(remaining)):
                generate_combination(prefix + [remaining[i]], remaining[:i] + remaining[i + 1:])

        generate_combination([], self.elements)
        return result

    def johnson_trotter(self):
        n = len(self.elements)
        result = []
        directions = [1] * n
        permutation = list(self.elements)

        def get_mobile_index():
            mobile_index = -1
            mobile_value = -1
            for i in range(n):
                if directions[i] == 1 and i < n - 1 and permutation[i] > permutation[i + 1]:
                    if permutation[i] > mobile_value:
                        mobile_value = permutation[i]
                        mobile_index = i
                elif directions[i] == 0 and i > 0 and permutation[i] > permutation[i - 1]:
                    if permutation[i] > mobile_value:
                        mobile_value = permutation[i]
                        mobile_index = i
            return mobile_index

        def generate_permutations():
            while True:
                mobile_index = get_mobile_index()
                if mobile_index == -1:
                    break

                swap_index = mobile_index + directions[mobile_index]
                permutation[mobile_index], permutation[swap_index] = permutation[swap_index], permutation[mobile_index]
                directions[mobile_index], directions[swap_index] = directions[swap_index], directions[mobile_index]

                result.append(permutation[:])

        result.append(permutation[:])
        generate_permutations()
        return result

    def itertools_combinations(self):
        result = []
        for r in range(1, len(self.elements) + 1):
            combinations = itertools.combinations(self.elements, r)
            result.extend(combinations)
        return result


elements = input('введите элементы списка для генерации комбинаций через пробел: ').split()
combinator = Combinator(elements)

print("алгоритм нарайаны:")
print(combinator.narayana())

print("\nалгоритм итертулс:")
print(combinator.itertools_combinations())
