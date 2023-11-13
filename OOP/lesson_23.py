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
