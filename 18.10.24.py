start = int(input())
if start == 1:
    n = int(input())
    a = 0
    while a <= n-1:
        a+=1
        print(a)
elif start == 2:
    a = int(input())
    b = int(input())
    while a <= b:
        print(a)
        a+=1
elif start == 3:
    def deg_two(n):
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

    n = int(input("введите число N: "))
    if deg_two(n):
        print("yes")
    else:
        print("no")