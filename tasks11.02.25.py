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

garlands(4, 4, 8)
teams(2, 2, 1, 5)
beads(4, 5, 6)
fruits(2, 3, 4)
bracelets(5, 6, 7)
