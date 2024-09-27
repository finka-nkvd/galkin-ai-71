start = int(input('введите номер задания '))
if start == 1:
    try: 
        num1 = int(input('введите число '))
        num2 = int(input("введите второе число на которое надо чтобы кратно было "))
    except: 
        print('нада цыферки')
        num1 = int(input('введите число '))
        num2 = int(input("введите второе число на которое надо чтобы кратно было "))
    if num1 % num2 == 0:
        print('работает')
    else:
        print('не работает')
elif start == 2:
    try:
        num1 = float(input('введивте первую циферку '))
        num2 = float(input('введтивте вторую циферку '))

    except:
        print('циферки циферки')
        num1 = float(input('введивте первую циферку '))
        num2 = float(input('введтивте вторую циферку '))
    itt = input('введитё иттерацию ')
    if itt == '+':
        print(num1 + num2)
    elif itt == '-':
        print(num1 - num2)
    elif itt == '*':
        print(num1 * num2)
    elif itt == '/':
        if num1 == 0 or num2 == 0:
            print('ты гений на ноль делить нельзя')
        else:
            print(num1 / num2)
elif start==3:
    num1 = float(input("введите циферку чтобы проверить на положительность"))
    if num1 > 0:
        print("положительно")
    else:
        print('отрицательно')
elif start==4:
    num1 = float(input('введите число чтобы проверить на четность'))
    if num1 % 2 == 0:
        print('четно')
    else:
        print("нечетно")
elif start==5:
    num1 = float(input('введите число чтобы проверить отрицательное положительное или 0'))
    if num1 == 0:
        print('ноль')
    elif num1 < 0:
        print('отрицательно')
    elif num1 > 0:
        print('положительно')
elif start == 6:
    num1 = int(input('введите число на проверку четности'))
    num2 = int(input('второе'))
    num3 = int(input('и третье'))
    if num1 % 2 == 0 or num2 % 2 == 0 or 3 % 2 == 0:
        print('есть четное')
elif start == 7:
    num = int(input('введите число чтобы проверить какое оно'))
    if num < 10:
        print('меньше 10')
    elif num >= 10 and num <=20:
        print('между 10 и 20')
    elif num > 20:
        print('больше 20')
elif start == 8:
    print('не доделано')
