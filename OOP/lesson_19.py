# 18 Специальные методы сравнения объектов классов

# __eq__ - отвечает за ==
# __ne__ - отвечает за !=
# __lt__ - отвечает за <
# __le__ - отвечает за <=
# __gt__ - отвечает за >
# __ge__ - отвечает за >=

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property  # 3. находим площадь прямоугольника, чтобы сравнить экземпляры знаком <
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        print('__eq__ вызван')
        if isinstance(other, Rect):  # 1. если поступающие данные равны нашему экземпляру класса
            return self.a == other.a and self.b == other.b  # 2. выводит True, если экземпляры равны

    def __lt__(self, other):  # 4. проверяем знаком меньше: <
        print('__lt__ вызван')
        if isinstance(other, Rect):
            return self.area < other.area
