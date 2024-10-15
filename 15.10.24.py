import math
start = int(input('введите номер задания: '))
if start == 1:
    def exchange(course, value, name):
        result = round(value/course, name)
        print(result)

    value = int(input('введите количество денег: '))
    name = input('введите название валюты: ')
    course = int(input('введите курс валюты: '))
    exchange(course, value, name)
elif start == 2:
    p = 3.14
    def square():
        a_sq = int(input('введите ширину прямоугольника: '))
        b_sq = int(input('ввудите высоту прямоугольника: '))
        result = (a_sq+b_sq)*2
        print(result, 'периметр прямоугольника')
        result = a_sq * b_sq
        print(result, 'площадь')
    def circle():
        radius = int(input('введите радиус круга: '))
        result = 2*p*radius
        print(result, 'периметр круга')
        result = (p*radius)**2
        print(result, 'площадь круга')
    def triangle():
        a_tr = int(input('введите 1 сторону треугольника: '))
        b_tr = int(input('введите 2 сторону треугольника: '))
        c_tr = int(input('введите 3 сторону треугольника: '))
        result = a_tr + b_tr + c_tr
        p = result / 2
        print(result, 'периметр треугольника')
        result = math.sqrt(p*(p-a_tr)*(p-b_tr)*(p-c_tr))
        print(result, 'площадь треугольника')
    def romb():
        a_r = int(input('введите сторону ромба: '))
        h_r = int(input('введите высоту ромба: '))
        result = a_r*4
        print(result, 'периметр ромба')
        result = a_r*h_r
        print(result, 'площадь ромба')

    square()
    circle()
    triangle()
    romb()
elif start == 3:
    def avg():
        nums = list(map(int, input('введите числа через пробел: ').split()))
        result = sum(nums)/len(nums)
        print(result)
    avg()
elif start == 4:
    def nod():
        n1 = int(input('введите первое число: '))
        n2 = int(input('введите первое число: '))
        print(math.gcd(n1, n2,), "НОД 2 чисел")
    nod()
elif start == 5:
    def triangle():
        a = int(input("введите первое число: "))
        b = int(input("введите второе число: "))
        c = a**2 + b**2
        print(c, '3 угол')
        p = (a+b+c)/2
        result = math.sqrt(p*(p-a)*(p-b)*(p-c))
        print(result, "площадь")
    triangle()
elif start == 6:
    def max_two(a, b):
        if a > b:
            return a
        return b
    nums = list(map(int, input('введите числа через пробел: ').split()))
    print(max_two(max_two(*nums[:2]), max_two(*nums[2:])))
elif start == 7:
    def fact():
        number = int(input('введите число: '))
        factorial = 1
        while number > 1:
            factorial = factorial * number
            number = number - 1
        print(factorial)
    fact()






