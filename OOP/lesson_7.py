# Практика по созданию классов

from math import sqrt  # импортируем функцию корня из библиотеки math

class Point:

    list_point = []  # создали список в который будем добавлять все новые точки в виде объектов с координатами

    def __init__(self, coord_x=0, coord_y=0):  # коорд передаем по умолчанию, чтобы не было ошибки при их отсутствии
        self.move_to(coord_x, coord_y)
        Point.list_point.append(self)  # внутри класса вызываем экземпляр через имя самого класса

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)  # используем уже созданный метод для упрощения кода

    def print_point(self): # делаем функцию красивого вывода данных о координатах точки
        print(f"Точки координат: ({self.x}, {self.y})")

    # найдем расстояние между двумя точками, применив теорему пифагора
    def distance(self, another_point):
        if not isinstance(another_point, Point):  # проверяем принадлежность экземпляра к классу
            raise ValueError('Аргумент не принадлежит классу Point') # вызываем исключение

        return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)


a = Point(6, 0)
b = Point(0, 8)

print (a.distance(b))

print(Point.list_point)
print(Point.list_point[0].x)  # по индексу мы обращаемся к объекту в списке и можем вывести координаты x и у
print(Point.list_point[0].y)
print(Point.list_point[1].x)
print(Point.list_point[1].y)


