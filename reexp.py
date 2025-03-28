import re

class Data:
    def __init__(self, name, phone_number, birth_date):
        self.name = name
        self.phone_number = phone_number
        self.birth_date = birth_date

    def birth_date_checker(self):
        reexp = r'\d\d-\d\d-\d{4}'
        matches = re.findall(reexp, self.birth_date)
        if matches:
            return True
        else:
            return False

    def phone_number_checker(self):
        reexp = r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}'
        matches = re.findall(reexp, self.phone_number)
        if matches:
            return True
        else:
            return False

    def name_checker(self):
        reexp = r'^[А-ЯA-Z].*'
        matches = re.findall(reexp, self.name)
        if matches:
            return True
        else:
            return False

class DataRecorder:
    def __init__(self, filename):
        self.filename = filename

    def record_data(self, data):
        if data.birth_date_checker() and data.phone_number_checker() and data.name_checker():
            with open(self.filename, 'a', encoding='utf-8') as file:
                file.write(f"имя: {data.name}\n")
                file.write(f"номер телефона: {data.phone_number}\n")
                file.write(f"дата рождения: {data.birth_date}\n\n")
            print("данные успешно записаны в файл.")
        else:
            print("данные не соответствуют формату.")

name = input("введите имя с заглавной буквы: ")
phone_number = input("введите номер телефона в формате +7(XXX)XXX-XX-XX: ")
birth_date = input("введите дату рождения в формате dd-mm-yyyy: ")
data = Data(name, phone_number, birth_date)
recorder = DataRecorder('data.txt')
recorder.record_data(data)
