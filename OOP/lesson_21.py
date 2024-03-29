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

    # метод __bool__ должен быть или положительным, или отрицательным, если он есть, метод __len__ не вызывается
    # задаем условие, что точка с координатами (0, 0) = False, остальные координаты = True
    def __bool__(self):
        print('__bool__ call')
        return self.x != 0 or self.y != 0

a = Point(3, 5)
print(f'0 Вызывается метод __bool__, точка {a} с координатами {a.x}, {a.y} :', bool(a))

b = Point(0, -5)
print(f'1 Вызывается метод __bool__, точка {b} с координатами {b.x}, {b.y} :', bool(b))

c = Point(34, 0)
print(f'2 Вызывается метод __bool__, точка {c} с координатами {c.x}, {c.y} :', bool(c))

d = Point(0, 0)
print(f'3 Вызывается метод __bool__, точка {d} с координатами {d.x}, {d.y} :', bool(d))


print('4', bool(44))  # число(кроме 0) всегда True
print('5', bool(-44))  # отрицательное число(кроме 0) всегда True
print('6', bool(0))  # 0 всегда False
print('7', bool('dhdhdhd'))  # не пустая строка всегда True
print('8', bool(''))  # пустая строка всегда False
print('9', bool(['dfhdfgh']))  # коллекции(словари, списки, строки) всегда True
print('10', bool([]))  # пустая коллекция False