import timeit

iter_code = """
from itertools import permutations
perms = ' '.join(map(lambda x: ''.join(x), permutations('толпа')))
words = perms.split()
"""

nar_code = """
from itertools import combinations
def all_subsets(word):
    n = len(word)
    result = []
    for r in range(1, n + 1):
        for comb in combinations(range(n), r):
            subset = ''.join(word[i] for i in comb)
            result.append(subset)
    return result
word = "толпа"
all_subsets(word)
"""

dj_code = """def johnson_trotter_words(word):
    n = len(word)
    perm = list(range(n))
    directions = [-1] * n
    permutations = []

    def to_word(p):
        return "".join(word[i] for i in p)

    def is_mobile(i):
        if directions[i] == -1 and i > 0:
            return word[perm[i]] > word[perm[i - 1]]
        elif directions[i] == 1 and i < n - 1:
            return word[perm[i]] > word[perm[i + 1]]
        else:
            return False

    permutations.append(to_word(perm))

    for i in range(120):
        mobile_index = -1
        for i in range(n):
            if is_mobile(i):
                if mobile_index == -1 or word[perm[i]] > word[perm[mobile_index]]:
                    mobile_index = i

        if mobile_index == 120:
            break

        swap_index = mobile_index + directions[mobile_index]

        perm[mobile_index], perm[swap_index] = perm[swap_index], perm[mobile_index]
        directions[mobile_index], directions[swap_index] = directions[swap_index], directions[mobile_index]

        for i in range(n):
            if word[perm[i]] > word[perm[mobile_index]]:
                directions[i] *= -1

        permutations.append(to_word(perm))

    return permutations

word = "толпа"
johnson_trotter_words(word)
"""

iter_time = timeit.timeit(iter_code, number=1)
print('время выполнения алгоритма itertools.permutations: ', iter_time)
nar_time = timeit.timeit(nar_code, number=1)
print('время выполнения алгоритма нарайаны: ', nar_time)
dj_time = timeit.timeit(dj_code, number=1)
print('время выполнения алгоритма джонсона-троттера: ', dj_time)
