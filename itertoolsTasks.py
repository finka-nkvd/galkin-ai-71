import itertools
start = int(input("введите номер задания: "))
if start == 1:
    perms = list(itertools.permutations(["Астра", "Вега", "Гриф"], 2))
    for perm in perms:
        print(perm)
elif start == 2:
    perms = list(itertools.permutations(["ребенок 1", "ребенок 2", "ребенок 3", "ребенок 4"], 3))
    for perm in perms:
        print(perm)
elif start == 3:
    print('этих ребят на олимпиаду')
    perms = list(itertools.permutations(["ребенок 1", "ребенок 2", "ребенок 3", "ребенок 4", "ребенок 5", "ребенок 6", "ребенок 7"], 2))
    for perm in perms:
        print(perm)
elif start == 4:
    perms = list(itertools.permutations(["книга 1", "книга 2", "книга 3", "книга 4", "книга 5", "книга 6", "книга 7", "книга 8", "книга 9", "книга 10"], 3))
    for perm in perms:
        print(perm)
    perms = list(itertools.permutations(["журнал 1", "журнал 2", "журнал 3", "журнал 4"], 2))
    for perm in perms:
        print(perm)
