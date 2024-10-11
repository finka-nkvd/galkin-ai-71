start = int(input('напишите номер задания: '))
if start == 1:
    def hello(name):
        print(f'Привет, {name}')
    hello(input('Введите имя: '))
elif start == 2:
    def b_math(n1, n2):
        print(n1 + n2)
        print(n1 - n2)
        print(n1 * n2)
        try:
            print(n1 / n2)
        except:
            print('на ноль делить нельзя')
    n1 = int(input())
    n2 = int(input())
    b_math(n1, n2)
elif start == 3:
    def sum(*params):
        result = 0
        for n in params: result += n
        return result

    sumOfNumbers1 = sum(1, 2, 3, 4, 5)   # 15
    sumOfNumbers2 = sum(3, 4, 5, 6)   # 18
    print(sumOfNumbers1)
    print(sumOfNumbers2)
elif start == 4:
    a = 0
    books = []
    def remove(books, x):
        books = books.pop([x])
    def add(books, name):
        books = books.append(name)
    while a < 1:
        print(books)
        act = input('что сделать со списком книг?\nудалить   добавить   очистить\n')
        if act == 'добавить':
            name = input('введите название книги: ')
            add(books, name)
        elif act == 'удалить':
            number = int(input('введите номер книги: '))
            x = number - 1
            remove(books, x)
        elif act == 'конец':
            a += 5
        elif act == 'очистить':
            books = []

