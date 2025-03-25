import model
class View:
    def display_menu(self, figures):
        print("Меню:")
        for key, value in figures.items():
            print(f"{key}. {value}")

    def calculate_properties(self, figure):
        if isinstance(figure, model.TwoDimensionalShape):
            print(f"Площадь: {figure.area()}")
            print(f"Периметр: {figure.perimeter()}")
        elif isinstance(figure, model.ThreeDimensionalShape):
            print(f"Площадь поверхности: {figure.area()}")
            if figure.perimeter() is not None:
                print(f"Периметр: {figure.perimeter()}")
            print(f"Объем: {figure.volume()}")
