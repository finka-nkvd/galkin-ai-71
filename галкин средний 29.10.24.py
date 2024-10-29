import math
import random
start = int(input('введите номер задания: '))
if start == 1:
    def x_more(x, lst):
        for i in lst:
            if i>=x:
                x+=i
        print(x)
    x = int(input('введите число: '))
    lst = []
    for i in range(10):
        lst.append(random.randint(1, 100))
    print(lst)
    x_more(x, lst)
elif start ==2:
    def ans(x, n):
        s = x**3+x**5+x*n
        print(s)
    x = int(input('введите число: '))
    n = int(input('введите ещё одно число: '))
    ans(x, n)
elif start == 3:
    def fib(n):
        if n == 1 or n == 2:
            return 1
        return fib(n - 1) + fib(n - 2)
    fib(int(input('введите количество ступеней чисел фибоначчи: ')))
