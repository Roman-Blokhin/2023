# Магические методы __len__ и __abs__

class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):  # функция, которая будет считать количество символов всех атрибутов наших экземпляров
        return len(self.name + self.surname)


class Otrezok:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def __abs__(self):
        return abs(self.point_2 - self.point_1)


# __len__

a = User('fdh', 'dfhf')
print(a.__len__())  # посчитали сумму символов у двух атрибутов

# __abs__

b = Otrezok(2, 90)  # считает разницу между точками
print(b.__abs__())

c = Otrezok(200, 90)  # разницу между точками из отрицательного числа преобразуется в положительное
print(c.__abs__())
