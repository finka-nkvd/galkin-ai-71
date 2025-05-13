from tkinter import *
task = int(input('введите номер задания (1-13): '))
if task == 1:
    root = Tk()
    root.title("10, 20")
    root.geometry('200x200+10+20')
    root.mainloop()
elif task == 2:
    root = Tk()
    root.title("2 задача")
    root.geometry('200x200')
    b1 = Button(text='1')
    b1.pack(side='left')
    b2 = Button(text='2')
    b2.pack(side='right')
    root.mainloop()
elif task == 3:
    print('недоделано')
elif task == 4:
    print('недоделано')
elif task == 5:
    print('недоделано')
elif task == 6:
    print('недоделано')
elif task == 7:
    print('недоделано')
elif task == 8:
    print('недоделано')
elif task == 9:
    print('недоделано')
elif task == 10:
    print('недоделано')
elif task == 11:
    print('недоделано')
elif task == 12:
    print('недоделано')
elif task == 13:
    print('недоделано')
else:
    print('других нет')