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

    def __eq__(self, other):
        print('__eq__ вызван')
        if isinstance(other, Rect):  # если поступающие данные равны нашему экземпляру класса
            return self.a == other.a and self.b == other.b  # выводит True, если экземпляры равны
