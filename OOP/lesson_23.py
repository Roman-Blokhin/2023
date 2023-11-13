# Магический метод __call__

class Counter:
    def __init__(self):  # инициализация
        self.name = 'Roman'
        self.counter = 0
        print(f'Объект инициализирован:', self.name)

    def __repr__(self):  # имя объекта понятно написано
        return f'Славный объект: {self.name}'

    def __call__(self, *args, **kwargs):  # можем теперь вызывать сам элемент: a() без замыкания
        self.counter += 1
        print(f'Объект {self.name} вызывался {self.counter} раз')

# --------------- Счетчик среднего значения без замыкания ---------------- #
class Count:
    def __init__(self):
        self.counter = 0
        self.summa = 0  # сумма
        self.length = 0  # длина
        print(f'Объект инициализирован:', self)

    def __call__(self, *args, **kwargs):  # можем теперь вызывать сам элемент: a() без замыкания
        self.counter += 1
        self.summa = sum(args)  # так как *args сохраняет значения в tuple и там будут числа, то сумму посчитает
        self.length = len(args)
        print(f'Объект {self} вызывался {self.counter} раз')

    def average(self):
        return self.summa/self.length
