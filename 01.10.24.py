import random
start = int(input('введите номер задания: '))
if start == 1:
    op = input('введите обозначение оператора: ')
    if op == '=':
          print(f'оператор (=)'
                f'c = 23 значит присваивание переменной с значение 23')
    elif op == '+=':
        c = 5
        a = 6
        print(f'оператор (+=)'
              f'c = 5',
              f'a = 6',
              f'c += a тоже самое что c = a+c что равно {c + a}',
              f'это сложение', sep='\n')
    elif op == '-=':
        c = 12
        a = 4
        print(f'оператор (-=)',
              f'c = 12',
              f'a = 4',
              f'c -= a тоже самое что с = с - а что равно {c - a}',
              f'это вычитание', sep='\n')
    elif op == '*=':
        c = 4
        a = 7
        print(f'оператор (*=)',
              f'c = 4',
              f'a = 7',
              f'c *= a тоже самое что с = с * а что равно {4 * 7}',
              f'это умножение', sep='\n')
    elif op == '/=':
        c = 42
        a = 6
        print(f'оператор (/=)',
              f'c = 42',
              f'a = 6',
              f'c /= a тоже самое что с = с / а что равно {c / a}',
              f'это деление', sep='\n')
    elif op == '%=':
        c = 5
        a = 2
        print(f'оператор (%=)',
              f'c = 5',
              f'a = 2',
              f'c %= a тоже самое что с = с % а что равно {5 % 2}',
              f'это деление по модулю', sep='\n')
    elif op == '**=':
        c = 2
        a = 3
        print(f'оператор (**=)',
              f'c = 2',
              f'a = 3',
              f'c **= a тоже самое что с = с ** а что равно {2 ** 3}',
              f'это возведение в степень', sep='\n')
    elif op == '//=':
        c = 11
        a = 2
        print(f'оператор (//=)',
              f'c = 11',
              f'a = 2',
              f'c //= a тоже самое что с = с // а что равно {11 // 2}',
              f'это целочисленное деление', sep='\n')
elif start == 2:
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(f'1 - {numbers[:: -1]}',
          f'2 - {numbers[:: 2]}',
          f'3 - {numbers[1::2]}',
          f'4 - {numbers[0:1]}',
          f'5 - {numbers[6:7]}',
          f'6 - {numbers[5:6]}',
          f'7 - {numbers[6:7]}',
          f'8 - {numbers[-3:1:-1]}',
          f'9 - {numbers[2:5]}', sep = '\n')

elif start == 3:
    numbers = list(map(int, input('введите числа через пробел: ').split())) #преобразуем много чисел в list
    n = numbers.count(int(input('введите нужное число: '))) #.count(n) - щтука чтобы посчитать сколько раз число повторяется в списке
    print(n)

elif start == 4:
    lst = [1,2,3,4,5,6,7,8,9,0]
    func = input('введите название функции листа (введите list чтобы увидеть лист):  ')
    if func == 'append':
        print('x.append(n) - добавляет элемент в конец списка, всегда возвращает "None" (x - название листа, n - элемент)')
        x = input('введите элемент чтобы добавить в конец списка: ')
        print(lst.append(x), '\nлист с новым элементом')
    elif func == 'extend':
        print('x.extend(n) - добавляет элементы из списка n в конец списка (x - название листа, n - название второго листа)')
        numbers = list(map(int, input('введите числа через пробел для второго листа: ').split()))
        print(lst.extend(numbers))
    elif func == 'insert':
        print('x.insert(i, l) - добавляет элемент l к элементу с индексом i в списке x')
        l = input('введите элемент l: ')
        i = int(input('введиет нужный индекс: '))
        print(lst.insert(i, l))
    elif func == 'remove':
        print('x.remove(i) - удаляет из списка x элементы с индексом i')
        i = int(input('введите индекс нужного числа: '))
        print(lst.remove(i))
    elif func == 'pop':
        print('x.pop([i]) - удаляет элемент с индексом i и выводит его')
        i = int(input('введите индекс жлемента для удаления: '))
        print(lst.pop([i]))
    else:
        print("доделать дома")

elif start == 5:
    itt = input('введите действие: ')
    if itt == 'площадь':
        height = int(input('введите ширину: '))
        length = int(input('введите высоту: '))
        print(height*length)
    elif itt == 'периметр':
        height = int(input('введите ширину: '))
        length = int(input('введите высоту: '))
        print((length+height)*2)
    elif itt == 'площадь круга':
        r = int(input('введите радиус: '))
        print((3.14*r)**2)

elif start == 6:
    n = int(input('введите кол-во столбцов: '))
    m = int(input('введите кол-во строк: '))
    matrix = [[random.randint(1, 10) for i in range(n)] for j in range(m)]
    #
    for row in matrix:
        for element in row:
            print(element, end='\t')  # Ставит в конце таб
        print()  # перенос строки
