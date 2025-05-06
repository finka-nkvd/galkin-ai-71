import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod


class BaseForm(ABC):
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    @abstractmethod
    def setup_ui(self):
        pass

    @abstractmethod
    def submit_form(self):
        pass

    def run(self):
        self.root.mainloop()


class ZooForm(BaseForm):
    def setup_ui(self):
        self.root.title("Форма заявки на работу в зоопарке")
        self.root.geometry("500x700")

        tk.Label(self.root, text='Форма заявки на работу в зоопарке',
                 font=("Times New Roman", 16, "bold")).pack()
        tk.Label(self.root,
                 text='Пожалуйста, заполните форму. Обязательные для заполнения поля обозначены знаком *',
                 font=("Times New Roman", 8, "italic")).pack()

        self.setup_contact_info()
        self.setup_personal_info()
        self.setup_animals()
        self.setup_submit_button()

    def setup_contact_info(self):
        frame = tk.LabelFrame(self.root, text="Контактная информация", padx=10, pady=10)
        frame.pack(pady=10, padx=10, fill="x")

        self.name_entry = self.create_labeled_entry(frame, "Имя *", 0)
        self.phone_entry = self.create_labeled_entry(frame, "Телефон", 1)
        self.email_entry = self.create_labeled_entry(frame, "Email *", 2)

    def setup_personal_info(self):
        frame = tk.LabelFrame(self.root, text="Персональная информация", padx=10, pady=10)
        frame.pack(pady=10, padx=10, fill="x")

        self.age_entry = self.create_labeled_entry(frame, "Возраст *", 0)

        tk.Label(frame, text="Пол").grid(row=1, column=0, sticky="w")
        self.gender_var = tk.StringVar(value="Женщина")
        tk.OptionMenu(frame, self.gender_var, "Женщина", "Мужчина", "Другой").grid(row=1, column=1, pady=5, sticky="w")

        tk.Label(frame, text="Перечислите личные качества").grid(row=2, column=0, sticky="nw")
        self.qualities_entry = tk.Text(frame, width=30, height=5)
        self.qualities_entry.grid(row=2, column=1, pady=5)

    def setup_animals(self):
        frame = tk.LabelFrame(self.root, text="Выберите ваших любимых животных", padx=10, pady=10)
        frame.pack(pady=10, padx=10, fill="x")

        animals = ["Зебра", "Кошак", "Анаконда", "Человек", "Слон", "Антилопа", "Голубь", "Краб"]
        self.animals_vars = {}

        for i, animal in enumerate(animals):
            self.animals_vars[animal] = tk.BooleanVar()
            cb = tk.Checkbutton(frame, text=animal, variable=self.animals_vars[animal])
            cb.grid(row=i // 2, column=i % 2, sticky="w", padx=5, pady=2)

    def setup_submit_button(self):
        tk.Button(self.root, text="Отправить информацию", command=self.submit_form).pack(pady=20)

    def create_labeled_entry(self, frame, label_text, row):
        tk.Label(frame, text=label_text).grid(row=row, column=0, sticky="w")
        entry = tk.Entry(frame, width=40)
        entry.grid(row=row, column=1, pady=5)
        return entry

    def submit_form(self):
        if not self.name_entry.get() or not self.email_entry.get() or not self.age_entry.get():
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все обязательные поля (*)")
            return

        selected_animals = [animal for animal, var in self.animals_vars.items() if var.get()]
        result = f"Контактная информация:\nИмя: {self.name_entry.get()}\nТелефон: {self.phone_entry.get()}\nEmail: {self.email_entry.get()}\n\n"
        result += f"Персональная информация:\nВозраст: {self.age_entry.get()}\nПол: {self.gender_var.get()}\nЛичные качества: {self.qualities_entry.get('1.0', tk.END)}\n\n"
        result += f"Любимые животные: {', '.join(selected_animals)}"

        messagebox.showinfo("Введенные данные", result)


class RegistrationForm(BaseForm):
    def setup_ui(self):
        self.root.title("Форма регистрации")
        self.root.geometry("500x550")

        self.required_style = {'fg': 'red', 'font': ("Arial", 10)}
        self.normal_style = {'font': ("Arial", 10)}

        self.setup_registration_fields()
        self.setup_delivery_info()
        self.setup_notifications()
        self.setup_submit_button()
        self.setup_footer()

    def setup_registration_fields(self):
        frame = tk.LabelFrame(self.root, text="Форма регистрации", padx=10, pady=10)
        frame.pack(pady=10, padx=10, fill="x")

        fields = [
            ("ФИО", 0, True),
            ("Email", 1, False),
            ("Номер телефона", 2, True),
            ("Город", 3, False),
            ("Дата рождения", 4, True)
        ]

        self.entries = {}
        for field, row, is_required in fields:
            field_frame = tk.Frame(frame)
            field_frame.grid(row=row, column=0, sticky="w", pady=5)

            tk.Label(field_frame, text=field, **self.normal_style).pack(side="left")
            if is_required:
                tk.Label(field_frame, text="*", **self.required_style).pack(side="left")

            entry = tk.Entry(frame, width=40)
            entry.grid(row=row, column=1, pady=5)
            self.entries[field] = entry

    def setup_delivery_info(self):
        frame = tk.LabelFrame(self.root, text="Параметры доставки", padx=10, pady=10)
        frame.pack(pady=10, padx=10, fill="x")

        self.address_entry = self.create_labeled_entry(frame, "Адрес", 0)
        self.zip_entry = self.create_labeled_entry(frame, "Почтовый индекс", 1)

    def setup_notifications(self):
        frame = tk.LabelFrame(self.root, text="Предпочитаемый способ получения уведомлений:", padx=10, pady=10)
        frame.pack(pady=10, padx=10, fill="x")

        self.notification_var = tk.StringVar(value="По Email")
        options = [
            ("По Email", "По Email"),
            ("По телефону", "По телефону"),
            ("Не уведомлять меня", "Не уведомлять меня")
        ]

        for text, value in options:
            tk.Radiobutton(frame, text=text, variable=self.notification_var, value=value).pack(anchor="w", pady=2)

    def setup_submit_button(self):
        tk.Button(self.root, text="Отправить данные", command=self.submit_form, padx=20, pady=5).pack(pady=20)

    def setup_footer(self):
        tk.Label(self.root, text="* - обязательные поля", fg="red", font=("Arial", 8)).pack()

    def create_labeled_entry(self, frame, label_text, row):
        tk.Label(frame, text=label_text).grid(row=row, column=0, sticky="w", pady=5)
        entry = tk.Entry(frame, width=40)
        entry.grid(row=row, column=1, pady=5)
        return entry

    def submit_form(self):
        if not self.entries["ФИО"].get() or not self.entries["Номер телефона"].get() or not self.entries[
            "Дата рождения"].get():
            messagebox.showerror("Ошибка", "Пожалуйста, заполните обязательные поля (*)")
            return

        result = f"Форма регистрации:\nФИО: {self.entries['ФИО'].get()}\nEmail: {self.entries['Email'].get()}\nТелефон: {self.entries['Номер телефона'].get()}\nГород: {self.entries['Город'].get()}\nДата рождения: {self.entries['Дата рождения'].get()}\n\n"
        result += f"Параметры доставки:\nАдрес: {self.address_entry.get()}\nПочтовый индекс: {self.zip_entry.get()}\n\n"
        result += f"Уведомления: {self.notification_var.get()}"

        messagebox.showinfo("Введенные данные", result)


class SchoolForm(BaseForm):
    def setup_ui(self):
        self.root.title("Школьная форма")
        self.root.geometry("500x400")

        self.interests_list = ["Компьютеры", "Спорт", "Искусство"]
        self.schedule = [
            "1-й урок 9.00 - 9.45",
            "2-й урок 10.00 - 10.45",
            "3-й урок 11.00 - 11.45",
            "4-й урок 12.00 - 12.45",
            "5-й урок 13.00 - 13.45"
        ]

        self.setup_name_section()
        self.setup_password_section()
        self.setup_interests()
        self.setup_schedule()
        self.setup_submit_button()

    def setup_name_section(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10, fill="x", padx=20)

        tk.Label(frame, text="Ваше имя").pack(side="left")
        self.name_entry = tk.Entry(frame, width=20)
        self.name_entry.pack(side="left", padx=10)
        self.name_entry.insert(0, "Вася")

        tk.Button(frame, text="Очистить форму", command=self.clear_form).pack(side="right")

    def setup_password_section(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10, fill="x", padx=20)

        tk.Label(frame, text="Введите пароль").pack(side="left")
        self.password_entry = tk.Entry(frame, width=20, show="*")
        self.password_entry.pack(side="left", padx=10)

        tk.Button(frame, text="Сброс пароля", command=self.reset_password).pack(side="right")

    def setup_interests(self):
        frame = tk.LabelFrame(self.root, text="Ваши интересы", padx=10, pady=10)
        frame.pack(pady=10, fill="x", padx=20)

        self.interest_vars = []
        for interest in self.interests_list:
            var = tk.BooleanVar()
            self.interest_vars.append(var)
            tk.Checkbutton(frame, text=interest, variable=var).pack(anchor="w")

    def setup_schedule(self):
        frame = tk.LabelFrame(self.root, text="Выберите урок", padx=10, pady=10)
        frame.pack(pady=10, fill="x", padx=20)

        self.schedule_var = tk.StringVar(value=self.schedule[0])
        tk.OptionMenu(frame, self.schedule_var, *self.schedule).pack(anchor="w")

    def setup_submit_button(self):
        tk.Button(self.root, text="Отправить форму", command=self.submit_form,
                  bg="#4CAF50", fg="white", padx=20, pady=5).pack(pady=20)

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        for var in self.interest_vars:
            var.set(False)
        self.schedule_var.set(self.schedule[0])
        messagebox.showinfo("Информация", "Форма очищена")

    def reset_password(self):
        self.password_entry.delete(0, tk.END)
        messagebox.showinfo("Информация", "Пароль сброшен")

    def submit_form(self):
        interests = [interest for interest, var in zip(self.interests_list, self.interest_vars) if var.get()]
        result = f"Школьная форма:\nИмя: {self.name_entry.get()}\nПароль: {'*' * len(self.password_entry.get())}\n\n"
        result += f"Интересы: {', '.join(interests) if interests else 'Нет'}\n"
        result += f"Выбранный урок: {self.schedule_var.get()}"

        messagebox.showinfo("Введенные данные", result)


class FormFactory:
    @staticmethod
    def create_form(choice):
        root = tk.Tk()
        if choice == 1:
            return ZooForm(root)
        elif choice == 2:
            return RegistrationForm(root)
        elif choice == 3:
            return SchoolForm(root)
        else:
            raise ValueError("Недопустимый выбор формы")


def menu():
    while True:
        try:
            choice = int(
                input('Введите номер формы: \n1: Работа в зоопарке\n2: Регистрация\n3: Школа\n0: Выход из программы\n'))
            if choice == 0:
                break

            form = FormFactory.create_form(choice)
            form.run()
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

menu()
