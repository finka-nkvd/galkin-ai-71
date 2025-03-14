import json
import pandas as pd

class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"Контакт {name} добавлен.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Контакт {name} удален.")
        else:
            print(f"Контакт {name} не найден.")

    def modify_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            print(f"Номер телефона для {name} изменен.")
        else:
            print(f"Контакт {name} не найден.")

    def get_contacts(self):
        return self.contacts


class Saver:
    def __init__(self, json_filename, excel_filename):
        self.json_filename = json_filename
        self.excel_filename = excel_filename

    def save_to_json(self, contacts):
        with open(self.json_filename, 'w', encoding='utf-8') as file:
            json.dump(contacts, file, indent=4, ensure_ascii=False)
        print(f"Данные сохранены в {self.json_filename}.")

    def load_from_json(self):
        try:
            with open(self.json_filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_to_excel(self, contacts):
        df = pd.DataFrame(list(contacts.items()), columns=['Имя', 'Телефон'])
        df.to_excel(self.excel_filename, index=False)
        print(f"Данные сохранены в {self.excel_filename}.")

    def load_from_excel(self):
        try:
            df = pd.read_excel(self.excel_filename)
            return dict(zip(df['Имя'], df['Телефон']))
        except FileNotFoundError:
            return {}


class PhonebookManager:
    def __init__(self, phonebook, saver):
        self.phonebook = phonebook
        self.saver = saver

    def run(self):
        while True:
            print("\nМеню:")
            print("1. Добавить/Удалить/Изменить контакт")
            print("2. Просмотреть контакты")
            print("3. Сохранить/Загрузить данные")
            print("4. Выход")

            choice = input("Введите номер действия: ")

            if choice == '1':
                action = input("Введите действие (add/remove/modify): ")
                name = input("Введите имя: ")
                if action == 'add':
                    phone = input("Введите номер телефона: ")
                    self.phonebook.add_contact(name, phone)
                elif action == 'remove':
                    self.phonebook.remove_contact(name)
                elif action == 'modify':
                    new_phone = input("Введите новый номер телефона: ")
                    self.phonebook.modify_contact(name, new_phone)
                else:
                    print("Неверное действие.")
            elif choice == '2':
                print(self.phonebook.get_contacts())
            elif choice == '3':
                action = input("Введите действие (save/load): ")
                format = input("Введите формат (json/excel): ")
                if action == 'save':
                    if format == 'json':
                        self.saver.save_to_json(self.phonebook.get_contacts())
                    elif format == 'excel':
                        self.saver.save_to_excel(self.phonebook.get_contacts())
                    else:
                        print("Неверный формат.")
                elif action == 'load':
                    if format == 'json':
                        self.phonebook.contacts = self.saver.load_from_json()
                        print("Данные загружены из JSON.")
                    elif format == 'excel':
                        self.phonebook.contacts = self.saver.load_from_excel()
                        print("Данные загружены из Excel.")
                    else:
                        print("Неверный формат.")
                else:
                    print("Неверное действие.")
            elif choice == '4':
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите действие из меню.")


phonebook = Phonebook()
saver = Saver('contacts.json', 'contacts.xlsx')
manager = PhonebookManager(phonebook, saver)
manager.run()
