class calc:
    def __init__(self, act, n1, n2):
        self.n1 = n1
        self.act = act
        self.n2 = n2

        def add(n1, n2):
            return n1 + n2
        def sub(n1, n2):
            return n1 - n2
        def div(n1, n2):
            return n1 / n2
        def mult(n1, n2):
            return n1 * n2
        def power(n1, n2):
            return n1**n2

        if self.act == '+' or '1':
            add(self.n1, self.n2)
        elif self.act == '-' or '2':
            sub(self.n1, self.n2)
        elif self.act == '/' or '3':
            try:
                div(self.n1, self.n2)
            except ZeroDivisionError:
                return 'на ноль делить нельзя'
        elif self.act == '*' or '4':
            mult(self.n1, self.n2)
        elif self.act == '**' or '5':
            power(self.n1, self.n2)
        else:
            return 'error'

print(calc(int(input('введите знак (1 = +, 2 = -, 3 = *, 4 = /, 5 = **): ')), input('введите первое число: '), int(input('введите второе число: '))))
