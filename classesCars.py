import time
class Car:
    def __init__(self, brand, manufacturer, engine_volume, body_type, color):
        self.brand = brand
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.body_type = body_type
        self.color = color


    def engine_start(self):
        print(f"Двигатель заведен")

    def engine_stop(self):
        print(f"Двигатель остановлен")

    def headlights_on(self):
        print(f"Фары включены")

    def headlights_off(self):
        print(f"Фары выключены")

    def info(self):
        print(f"Бренд: {self.brand}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Объем двигателя: {self.engine_volume}")
        print(f"Тип кузова: {self.body_type}")
        print(f"Цвет: {self.color}")

AeroSwift = Car('AeroSwift', 'AeroTech Motors', '1.8 л (турбированный)', 'Седан', 'Перламутрово-белый')
AeroSwift.info()
AeroSwift.engine_start()
AeroSwift.engine_stop()
AeroSwift.headlights_on()
AeroSwift.headlights_off()
time.sleep(1)
print('\n')
TerraCruise = Car('TerraCruise', 'Terra Automotive Group', '3.0 л (дизель)', 'Внедорожник', 'Графитово-серый')
TerraCruise.info()
TerraCruise.engine_start()
TerraCruise.engine_stop()
TerraCruise.headlights_on()
TerraCruise.headlights_off()
time.sleep(1)
print('\n')
VoltRunner = Car('VoltRunner', 'ElectroMotion Corp.', 'Электромотор (мощность: 150 кВт)', 'Кроссовер', 'Ярко-зеленый металлик')
VoltRunner.info()
VoltRunner.engine_start()
VoltRunner.engine_stop()
VoltRunner.headlights_on()
VoltRunner.headlights_off()
time.sleep(1)
print('\n')

