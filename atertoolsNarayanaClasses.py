import itertools


class Combinator:
    def __init__(self, elements):
        self.elements = elements

    def johnson_trotter(self):
        n = len(self.elements)
        elements = self.elements.copy()
        directions = [-1] * n

        def find_mobile():
            max_mobile = float('-inf')
            mobile_pos = -1
            for i in range(n):
                if (directions[i] == -1 and i > 0 and elements[i] > elements[i - 1]) or \
                        (directions[i] == 1 and i < n - 1 and elements[i] > elements[i + 1]):
                    if elements[i] > max_mobile:
                        max_mobile = elements[i]
                        mobile_pos = i
            return mobile_pos

        def swap(i, j):
            elements[i], elements[j] = elements[j], elements[i]
            directions[i], directions[j] = directions[j], directions[i]

        def reverse_direction(mobile):
            for i in range(n):
                if elements[i] > mobile:
                    directions[i] *= -1

        permutations = [elements.copy()]

        while True:
            mobile_pos = find_mobile()
            if mobile_pos == -1:
                break

            mobile = elements[mobile_pos]
            if directions[mobile_pos] == -1:
                swap(mobile_pos, mobile_pos - 1)
            else:
                swap(mobile_pos, mobile_pos + 1)

            reverse_direction(mobile)
            permutations.append(elements.copy())

        return permutations

    def iter(self):
        return list(set(itertools.permutations(self.elements)))

    def narayana(self):
        n = len(self.elements)

        def generate(arr, i):
            if i == n:
                yield arr.copy()
            else:
                for j in range(i, n):
                    arr[i], arr[j] = arr[j], arr[i]
                    yield from generate(arr, i + 1)
                    arr[i], arr[j] = arr[j], arr[i]

        yield from generate(self.elements.copy(), 0)


combinator = Combinator([1, 2, 4])

print(combinator.johnson_trotter())
print(combinator.iter())
print(list(combinator.narayana()))
