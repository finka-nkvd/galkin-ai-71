import tkinter as tk
from PIL import Image, ImageTk

def b():
    print('hello world')

def win():
    root1 = tk.Tk()
    button = tk.Button(root1, text="На весь экран")
    button.pack(fill=tk.BOTH, expand=True)
    root1.mainloop()

def form():
    def ne_clear():
        name_entry.delete(0, tk.END)

    def le_clear():
        lastname_entry.delete(0, tk.END)

    def proceed():
        ans_root = tk.Tk()
        ans_root.geometry('150x75')
        ans_root.title("Результаты")
        name = name_entry.get()
        lastname = lastname_entry.get()
        ans_name_label = tk.Label(ans_root, text=f'Имя: {name}')
        ans_lname_label = tk.Label(ans_root, text=f'Фамилия: {lastname}')
        ans_name_label.pack(pady=5)
        ans_lname_label.pack(pady=5)
        ans_root.mainloop()

    form_root = tk.Tk()
    form_root.geometry('300x150')
    form_root.title("Форма для заполнения")

    label = tk.Label(form_root, text='Форма для заполнения:')
    label.grid(row=0, column=0, columnspan=3, pady=(10, 10))

    name_label = tk.Label(form_root, text='Введите имя:')
    name_label.grid(row=1, column=0, sticky='w', padx=5)
    name_entry = tk.Entry(form_root)
    name_entry.grid(row=1, column=1, padx=5)
    ne_clear_btn = tk.Button(form_root, text='✕', command=ne_clear)
    ne_clear_btn.grid(row=1, column=2, padx=5)

    lastname_label = tk.Label(form_root, text='Введите фамилию:')
    lastname_label.grid(row=2, column=0, sticky='w', padx=5, pady=(10, 0))
    lastname_entry = tk.Entry(form_root)
    lastname_entry.grid(row=2, column=1, padx=5, pady=(10, 0))
    le_clear_btn = tk.Button(form_root, text='✕', command=le_clear)
    le_clear_btn.grid(row=2, column=2, padx=5, pady=(10, 0))

    proceed_button = tk.Button(form_root, text='Готово', command=proceed)
    proceed_button.grid(row=3, column=0, columnspan=3, pady=(15, 0))

    form_root.mainloop()


root = tk.Tk()
root.title("1;1")
root.geometry("1000x1000+1+1")

img1_normal = ImageTk.PhotoImage(Image.open('number1.jpg'))
img1_hover = ImageTk.PhotoImage(Image.open('1number.jpg'))

img2_normal = ImageTk.PhotoImage(Image.open('number2.jpg'))
img2_hover = ImageTk.PhotoImage(Image.open('2number.jpg'))


def on_enter_b1(event):
    b1.config(image=img1_hover)


def on_leave_b1(event):
    b1.config(image=img1_normal)


def on_enter_b2(event):
    b2.config(image=img2_hover)


def on_leave_b2(event):
    b2.config(image=img2_normal)


b1 = tk.Button(root, text='1', image=img1_normal, compound='top', command=b)
b2 = tk.Button(root, text='2', image=img2_normal, compound='top', command=b)
b3 = tk.Button(root, text='2 окно', command=win)
form_b = tk.Button(root, text='форма', command=form)
form_b.pack()
b1.pack(side='left', padx=5)
b2.pack(side='right', padx=5)
b3.pack(side='left', anchor='s')

b1.bind("<Enter>", on_enter_b1)
b1.bind("<Leave>", on_leave_b1)
b2.bind("<Enter>", on_enter_b2)
b2.bind("<Leave>", on_leave_b2)

frame = tk.Frame(root)
frame.pack(side='bottom', pady=20)

buttons = []
for row in range(3):
    for col in range(3):
        btn = tk.Button(frame, text=f"{row*3+col+1}", width=8, height=3, command=b)
        btn.grid(row=row, column=col, padx=2, pady=2)
        buttons.append(btn)

label = tk.Label(root, text='текст')
label.pack()

root.configure(bg="#FFF8DC")
root.mainloop()
