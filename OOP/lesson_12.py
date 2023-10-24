# Property Вычисляемые свойства

class Square:  # 1. делаем класс по определению площади
    def __init__(self, s):
        self.side = s  # 2. задаем размер стороны квадрата

    @property  # 4. делаем декоратор, чтобы наша функция стала свойством, чтобы мы могли менять размер стороны
    def area(self):  # 3. метод по нахождению площади квадрата
        return self.side ** 2


# 5. теперь, после декоратора @property мы можем изменять размер нашей стороны квадрата
a = Square(6)  # 6. присвоили размер
print(a.area)
a.side = 90  # 7. переопределили размер
print(a.area)


# -------------------------------------------------------- #

class Square_2:
    def __init__(self, q):
        self.side = q
        self.__area = None  # 1. делаем приватную переменную с первоначальным значением None

    @property
    def area_2(self):
        if self.__area is None:  # 2. делаем проверку на первоначальное значение
            print('calculate area')  # 4. делаем отметку, когда у нас присваивается значение нашей переменной
            self.__area = self.side ** 2  # 3. присваиваем новое значение, оно кешируется и сохраняется
        return self.__area


# -------------------------------------------------------- #

# так как у нас сторона (side) теперь кешируется и не изменяется, мы должны сделать ее изменяемой, вернув значение None

class Square_3:
    def __init__(self, q):
        self.__side = q  # 1. делаем переменную стороны приватной
        self.__area = None

    # 2. создаем новый декоратор для нашей переменной стороны (side)
    @property  # 3. ГЕТТЕР
    def side(self):
        return self.__side

    @side.setter  # 4. СЕТТЕР
    def side(self, value):
        self.__side = value  # 5. передаем новое значение в SIDE
        self.__area = None  # 6. а __area вновь делаем со значением None

    @property
    def area_3(self):
        if self.__area is None:
            print('calculate area')
            self.__area = self.side ** 2
        return self.__area


d = Square_3(8)  # задаем значение
print(d.area_3)  # производится вычисление, значение кешируется, выводится отметка, что было вычисление
print(d.area_3)  # при новом вызове получаем только результат вычислений
d.side = 99  # задаем новое значение для нашей стороны
print(d.area_3)  # производится новое вычисление и вывод с отметкой


# --------------------------------------- #
# Будем искать периметр

class Perimetr:
    def __init__(self, p, pp):  # 1. создали функцию, которая принимает значение двух сторон
        self.__side_a = p  # 5. изменяем переменную сторон на приватные
        self.__side_b = pp  # 6. изменяем переменную сторон на приватные
        self.__inner = None  # 3. задаем первичное значение приватной переменной __inner = None

    @property  # 7. создаем новый декоратор для нашей переменной стороны А - ГЕТТЕР
    def side_1(self):
        return self.__side_a

    @property  # 8. создаем новый декоратор для нашей переменной стороны Б - ГЕТТЕР
    def side_2(self):
        return self.__side_b

    @side_1.setter  # 8. новый декоратор - СЕТТЕР, для изменения стороны А
    def side_1(self, value):
        self.__side_a = value
        self.__inner = None

    @side_2.setter  # 8. новый декоратор - СЕТТЕР, для изменения стороны Б
    def side_2(self, value):
        self.__side_b = value
        self.__inner = None

    @property
    def inner(self):  # 2. декорированная функция, которая высчитывает периметр по формуле
        if self.__inner is None:  # 4. делаем проверку, чтобы увидеть, что значение записывается в кеш
            print('Записано в кеш')
            self.__inner = (self.__side_a + self.__side_b) * 2
        return self.__inner

# ---------------------------- #
# Ищем площадь прямоугольника s = a*b

class Priam:
    def __init__(self, a, b):
        self.__side_1 = a
        self.__side_2 = b
        self.__result = None

    @property
    def side_1(self):
        return self.__side_2

    @property
    def side_2(self):
        return self.__side_2

    @side_1.setter
    def side_1(self, value):
        self.__side_1 = value
        self.__result = None

    @side_2.setter
    def side_2(self, value):
        self.__side_2 = value
        self.__result = None

    @property
    def result(self):
        if self.__result is None:
            print('Результат записан')
            self.__result = self.__side_1 * self.__side_2

        return self.__result