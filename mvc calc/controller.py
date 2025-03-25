import model, view
class Controller:
    def __init__(self):
        self.figures = {
            '1': 'круг',
            '2': 'квадрат',
            '3': 'прямоугольник',
            '4': 'треугольник',
            '5': 'сфера',
            '6': 'куб',
            '7': 'цилиндр',
        }
        self.view = view.View()
    def create_figure(self, choice):
        if choice == '1':
            radius = float(input('Введите радиус круга: '))
            return model.Circle(radius)
        elif choice == '2':
            side = float(input('Введите сторону квадрата: '))
            return model.Square(side)
        elif choice == '3':
            length = float(input('Введите длину прямоугольника: '))
            width = float(input('Введите ширину прямоугольника: '))
            return model.Rectangle(length, width)
        elif choice == '4':
            side1 = float(input('Введите первую сторону треугольника: '))
            side2 = float(input('Введите вторую сторону треугольника: '))
            side3 = float(input('Введите третью сторону треугольника: '))
            return model.Triangle(side1, side2, side3)
        elif choice == '5':
            radius = float(input('Введите радиус сферы: '))
            return model.Sphere(radius)
        elif choice == '6':
            side = float(input('Введите сторону куба: '))
            return model.Cube(side)
        elif choice == '7':
            radius = float(input('Введите радиус цилиндра: '))
            height = float(input('Введите высоту цилиндра: '))
            return model.Cylinder(radius, height)
        else:
            print("Недопустимый выбор.")
            return None

    def main(self):
        while True:
            self.view.display_menu(self.figures)
            choice = input("Выберите фигуру (или 'q' для выхода): ")
            if choice.lower() == 'q':
                break
            figure = self.create_figure(choice)
            if figure:
                self.view.calculate_properties(figure)

controller = Controller()
controller.main()
