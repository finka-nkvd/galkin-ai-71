import math
def calculate_combinations(counts):
    total_items = sum(counts)
    denominator = 1
    for count in counts:
        denominator *= math.factorial(count)
    return math.factorial(total_items) // denominator

def garlands(red, blue, yellow):
    print(calculate_combinations([red, blue, yellow]))

def teams(bandits, police, detective, bypassers):
    print(calculate_combinations([bandits, police, detective, bypassers]))

def beads(green, blue, red):
    print(calculate_combinations([green, blue, red]))

def fruits(apples, fruit, oranges):
    print(calculate_combinations([apples, fruit, oranges]))

def bracelets(emeralds, rubins, sapphires):
    print(calculate_combinations([emeralds, rubins, sapphires]))
    
task = int(input("введите номер задания: "))

if task == 1:
    garlands(4, 4, 8)
elif task == 2:
    teams(2, 2, 1, 5)
elif task == 3:
    beads(4, 5, 6)
elif task == 4:
    fruits(2, 3, 4)
elif task == 5:
    bracelets(5, 6, 7)
else:
    print("больше нету")
