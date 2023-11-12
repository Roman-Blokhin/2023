# Магический метод __call__

class Counter:
    def __init__(self, name):  # инициализация
        self.name = name
        print(f'Объект инициализирован:', self.name)

    def __repr__(self):  # имя объекта понятно написано
        return f'Славный объект: {self.name}'

    def __call__(self, *args, **kwargs):  # можем теперь вызывать сам элемент: a()
        print(f'Объект {self.name} вызван')