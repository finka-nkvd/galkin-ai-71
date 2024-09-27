start = int(input('введите номер задания '))
if start == 1:
    try: num1 = int(input('введите число '))
    except: print('нада цыферки')
    try: num2 = int(input("введите второе число на которое надо чтобы кратно было "))
    except: print('нада цыферки')
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
