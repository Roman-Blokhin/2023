# Магический метод __bool__ Правдивость объектов в Python
# Проверяет правдивость данных

# если у нас не реализован метод __bool__, то вызывается метод __len__, по принципу: пустое ли значение или нет
# если не реализованы ни __bool__ ни __len__ то значение всегда будет положительным

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__ call')
        return abs(self.x - self.y)

a = Point(3, 5)
print('0 Вызывается метод __len__ :', bool(a))


print('1', bool(44))  # число(кроме 0) всегда True
print('2', bool(-44))  # отрицательное число(кроме 0) всегда True
print('3', bool(0))  # 0 всегда False
print('4', bool('dhdhdhd'))  # не пустая строка всегда True
print('5', bool(''))  # пустая строка всегда False
print('6', bool(['dfhdfgh']))  # коллекции(словари, списки, строки) всегда True
print('7', bool([]))  # пустая коллекция False