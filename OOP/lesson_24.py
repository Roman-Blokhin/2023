# Магические методы __getitem__ , __setitem__ и __delitem__
# с помощью них можно добавить обращения по индексу к нашим объектам
# изначально классы не поддерживают операцию индексирования

class Vector:
    def __init__(self, *args):  # принимает на вход любое количество аргументов
        self.values = list(args)  # создаем список в который добавляются при их определении

    def __repr__(self):  # для отображения наших атрибутов в консоли
        return str(self.values)

    def __getitem__(self, item):  # функция, которая выводит атрибут по индексу в коллекции, item - индекс
        if 0 <= item < len(self.values):  # условие, что item(индекс) лежит в пределах от 0 до макс. в нашем массиве
            return self.values[item]  # возвращаем атрибут по индексу
        else:
            raise IndexError ('Индекс за пределами космического пространства')  # условие, если индекса нет в списке
        
    def __setitem__(self, key, value):  # функция, которая меняет значение аргумента по индексу
        if 0 <= key < len(self.values):  # key(ключ) - это индекс, values - новое значение
            self.values[key] = value  # присваиваем новое значение по индексу
        else:
            raise IndexError ('Индекс за пределами космического пространства')

    def __delitem__(self, key):  # удаляет аргумент по индексу, key - индекс
        if 0 <= key < len(self.values):
            del self.values[key]  # удалить значение у объекта по индексу key
        else:
            raise IndexError ('Индекс за пределами космического пространства')

# МЫ МОЖЕМ ИЗМЕНИТЬ ОБРАЩЕНИЕ ПО ЭЛЕМЕНТУ, ИНДЕКС БУДЕТ НАЧИНАТЬСЯ НЕ С 0, А С 1

class Vect:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 1 <= item <= len(self.values):  # условие поиска индекса от 1 до максимальной длины списка включительно
            return self.values[item-1]  # значение устанавливаем -1, искусственно уменьшаем значение индекса

# СОЗДАЕМ РАЗРЯЖЕННЫЙ МАССИВ, КОЛЛЕКЦИЯ, В КОТОРОЙ НЕКОТОРЫЕ ЗНАЧЕНИЯ(ИНДЕКСЫ) ПРОПУШЕНЫ [1,2,4,..,..,..,89]

class Vec:  # индекс у нас начинается с 1, мы изменили эти параметры в __getitem__ и __setitem__
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 1 <= item < len(self.values):
            return self.values[item-1]
        else:
            raise IndexError ('Индекс за пределами космического пространства')

    def __setitem__(self, key, value):
        if 1 <= key < len(self.values):
            self.values[key-1] = value
        elif key > len(self.values):  # если число больше, чем длина коллекции:
            diff = key - len(self.values)  # находим разницу между искомым индексом и крайним индексом в коллекции
            self.values.extend([None]*diff)  # расширяем список с помощью метода extend. Ставим нули по числу разницы
            self.values[key-1] = value  # обращаемся к нашему ключу(индексу) и присваиваем новое значение value
        else:
            raise IndexError ('Индекс за пределами космического пространства')