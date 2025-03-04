class cube_vol:
    def __init__(self, a):
        self.a = a

    def main(self):
        return self.a**3

class pyramid_vol:
    def __init__(self, s, h):
        self.s = s
        self.h = h

    def main(self):
        return 1/3*self.s*self.h

class sphere_vol:
    def __init__(self, r):
        self.r = r

    def main(self):
        return 4/3*3.14*self.r**3

class menu:
    def __init__(self):
        self.run()

    def run(self):
        while True:
            figure = input('введите фигуру для нахождения объема (0. выход, 1. куб, 2. сфера, 3. пирамида): ')
            if figure == 'куб' or figure == '1':
                a = float(input('введите сторону куба: '))
                print(cube_vol(a).main())
            elif figure == 'пирамида' or figure == '3':
                s = float(input('введите площадь основания: '))
                h = float(input('введите высоту пирамиды: '))
                print(pyramid_vol(s, h).main())
            elif figure == 'сфера' or figure == '2':
                r = float(input('введите радиус сферы: '))
                print(sphere_vol(r).main())
            elif figure == 'выход' or figure == '0':
                break

menu()
