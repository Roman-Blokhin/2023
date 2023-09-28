# МОНОСОСТОЯНИЕ У ВСЕХ ЭКЗЕМПЛЯРОВ КЛАССА

class Cat:
    __shared_attr = { # создаем приватную переменную, в которой будут значения для всех атрибутов в виде словаря
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):  # при добавлении нового атрибута он будет добавляться всем экземплярам класса
        self.__dict__ = Cat.__shared_attr

a = Cat()
print(a)

b = Cat()
b.name = 'sonia'
print(a.breed)
print(a.name)
a.breed = 'siam'
print(a.breed)
print(b.breed)
