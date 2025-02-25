class calc:
    def __init__(self, act, n1, n2):
        self.n1 = n1
        self.act = act
        self.n2 = n2

        def add(n1, n2):
            print(n1 + n2)
        def sub(n1, n2):
            print(n1 - n2)
        def div(n1, n2):
            print(n1 / n2)
        def mult(n1, n2):
            print(n1 * n2)

        if self.act == '+':
            add(self.n1, self.n2)
        if self.act == '-':
            sub(self.n1, self.n2)
        if self.act == '/':
            div(self.n1, self.n2)
        if self.act == '*':
            mult(self.n1, self.n2)

calc(int(input('введите знак (+, -, * или /): ')), input('введите первое число: '), int(input('введите второе число: ')))
