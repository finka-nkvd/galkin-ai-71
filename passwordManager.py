import pandas as pd
import os
from openpyxl import Workbook


class PasswordManager:
    _instances = {}

    def __new__(cls, account):
        if account not in cls._instances:
            instance = super(PasswordManager, cls).__new__(cls)
            instance.account = account
            instance.password = None
            cls._instances[account] = instance
            instance.load_password()
        return cls._instances[account]

    def load_password(self):
        file_path = 'passwords.xlsx'
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
            if self.account in df['Account'].values:
                self.password = df.loc[df['Account'] == self.account, 'Password'].iloc[0]
        else:
            print("Файл passwords.xlsx не найден.")

    def set_password(self, password):
        self.password = password
        self.save_password()

    def save_password(self):
        file_path = 'passwords.xlsx'
        data = {
            'Account': [],
            'Password': []
        }

        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
            if self.account in df['Account'].values:
                df.loc[df['Account'] == self.account, 'Password'] = self.password
            else:
                df.loc[len(df.index)] = [self.account, self.password]
            df.to_excel(file_path, index=False)
        else:
            data['Account'].append(self.account)
            data['Password'].append(self.password)
            df = pd.DataFrame(data)
            df.to_excel(file_path, index=False)

    def get_password(self):
        return self.password


def show_menu():
    print("\nМеню менеджера паролей:")
    print("1. Создать учетную запись")
    print("2. Установить пароль для учетной записи")
    print("3. Получить пароль для учетной записи")
    print("4. Выход")


def main():
    while True:
        show_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            account = input("Введите имя учетной записи: ")
            pm = PasswordManager(account)
            print(f"Учетная запись '{account}' создана.")

        elif choice == "2":
            account = input("Введите имя учетной записи: ")
            pm = PasswordManager(account)
            password = input("Введите пароль: ")
            pm.set_password(password)
            print(f"Пароль для учетной записи '{account}' установлен.")

        elif choice == "3":
            account = input("Введите имя учетной записи: ")
            pm = PasswordManager(account)
            password = pm.get_password()
            if password:
                print(f"Пароль для учетной записи '{account}': {password}")
            else:
                print(f"Пароль для учетной записи '{account}' не установлен.")

        elif choice == "4":
            print("Выход из программы.")
            break

        else:
            print("Недопустимый выбор")


main()
