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
