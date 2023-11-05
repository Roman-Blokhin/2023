# Магические методы __eq__ и __hash__
# __eq__ - метод для сравнения объектов
# __hash__ - изменяет наши данные в фиксированное числовое значение, обратно вернуть значение нельзя

class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):  # меняем описание экземпляра со стороны backend
        return f'{self.name} с координатами ({self.x}, {self.y})'

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y


p1 = Point('p1', 1, 2)
p2 = Point('p2', 1, 2)
p3 = Point('p2', 2, 8)
p4 = Point('p2', 2, 4)
print(f'1. Принадлежит ли {p1} к классу:', isinstance(p1, object))  # проверяем, принадлежит ли объект классу
print(f'2. id {p1} =', id(p1))  # узнаем id экземпляра в классе
print(f'3. id {p2} =', id(p2))
print(f'4. Равенство объектов: {p1} и {p2} =', p1 == p2)  # сравниваются по id, если нет магического метода сравнения

# __hash__
# print(f'5. Хешируем {p3} через магический метод:', p3.__hash__())
# print(f'6. Хешируем {p4} через встроенную функцию:', hash(p4))
