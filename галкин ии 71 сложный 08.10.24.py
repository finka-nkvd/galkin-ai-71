import random
start = int(input('введите номер задания: '))
if start == 1:
    list = [1, 2, 3, 4, 5, 12, -2]
    print(list, 'вот такой список')
    c = 0
    for i in list:
        if i >= 0:
            c = c+i
    print(c, 'сумма всех элементов')
elif start == 2:
    n = int(input('введите число: '))
    a = int(input('введите нижнее значение промежутка: '))
    b = int(input('введите высшее значение промежутка: '))
    if n >= a and n <= b:
        print('в промежутке')
    else:
        print('не в промежутке')
elif start == 3:
    n = int(input('введите количество случайных чисел: '))
    a = int(input('введите минимальное число: '))
    b =int(input('введите максимальное число: '))
    random_list = []
    for i in range(n):
        random_list.append(random.randint(a, b))
        list = sorted(random_list)
    print(list)
    n = n-1
    print(list[0], 'минимальное сгенерированное число \n', list[n], 'максимальное сгенерированное число')



