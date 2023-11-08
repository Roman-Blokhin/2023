# Полиморфизм в Python

class Rectangle:  # площадь прямоугольника
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_rect_area(self):
        return self.a * self.b


class Square:  # площадь квадрата
    def __init__(self, a):
        self.a = a

    def get_sq_area(self):
        return self.a ** 2


class Circle:  # площадь круга
    def __init__(self, r):
        self.r = r

    def get_circle_area(self):
        return 3.14 * self.r ** 2


# создаем экземпляры разных классов
rect = Rectangle(1, 2)
square = Square(5)
circle = Circle(7)

print('\n1. Площадь прямоугольника:', rect.get_rect_area(),
      '\n2. Площадь квадрата:', square.get_sq_area(),
      '\n3. Площадь круга:', circle.get_circle_area())

# 1. Если нам нужно обойти все объекты, то мы добавляем их в коллекцию/список и проводим через цикл for
# Возникнет ошибка, потому что все объекты - это экземпляры разных классов
# 2. Так как фигуры принадлежат разным классам, то обратиться к ним мы можем через - if else

figures = [rect, square, circle]

for fig in figures:
    if isinstance(fig, Rectangle):
        print('\n3. Прямоугольник:', rect.get_rect_area())
    elif isinstance(fig, Square):
        print('4. Квадрат:', square.get_sq_area())
    else:
        print('5. Круг:', circle.get_circle_area())

# 3. Чтобы не пропускать все через if else и не было ошибки, мы можем использовать ПОЛИМОРФИЗМ
