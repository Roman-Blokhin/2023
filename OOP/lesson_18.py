# Магические методы __add__, __mul__, __sub__ и __truediv__
# отвечают за базовые математические операции

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):  # 1. сложение, нужен второй аргумент, первый - наш клиент, второй - новый баланс
        print('__add__ был вызван')
        if isinstance(other, BankAccount):  # 3. проверка, если второй аргумент - экземпляр класса, то складываем
            return self.balance + other.balance  # 4. берем у экземпляра класса значение баланса
        if isinstance(other, (int, float)):  # 2. если значение принадлежит к типам int или float
            return self.balance + other
        raise NotImplemented  # 5. говорим, что для остальных типов операция не поддерживается

    def __radd__(self, other):
        print('__radd__ вызван')
        return self + other  # 6. мы поменяли местами наши слагаемые, новое значение ставим слева, чтобы не было ошибки

    def __mul__(self, other):  # 7. умножение
        print('__mul__ был вызван')
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, str):  # 8. проверка, проверяет тип значения, если строка, конкатенация в начало имени
            return other + self.name
        raise NotImplemented

    def __sub__(self, other):  # 7. вычитание
        print('__sub__ вызван')
        if isinstance(other, BankAccount):
            return self.balance - other.balance
        if isinstance(other, (int, float)):
            return self.balance - other
        raise NotImplemented

    def __truediv__(self, other):  # 7. деление/ можем делить экземпляр на экземпляр, меняя местами
        print('__truediv__ вызван')
        if isinstance(other, BankAccount):
            return self.balance / other.balance
        if isinstance(other, (int, float)):
            return self.balance / other
        raise NotImplemented


# ------------------- #

q = BankAccount('oi', 100)
w = BankAccount('oi', 1)
print(q + w)  # 4.1 можно менять местами элементы при сложении. экземпляры класса, а не экземпляр + новоезнач.
print(w + q)

r = BankAccount('aa', 1)  # 6.1 с помощью __radd__ мы можем менять слагаемые местами без ошибки
print(12 + r)

y = BankAccount('AA', 1)  # 8.1 с помощью __radd__ мы можем менять слагаемые местами без ошибки
print(y * 4)
print(y * 'oooooooo')


# ------------------- #

# Сделаем класс с магическим методом __add__, которое будет сохранять значение элементов при сложении
class Person:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'Новый пользователь {self.name} с балансом {self.balance}'

    def __add__(self, value):
        print('НОВЫЙ МЕТОД СЛОЖЕНИЯ')
        if isinstance(value, Person):
            return Person(self.name, self.balance + value.balance)
        if isinstance(value, (int, float)):
            return Person(self.name, self.balance + value)
        raise NotImplemented


a = Person('rot', 60)
b = Person('tort', 9)

d = a + 70  # новый экземпляр создается с сохранением имени и нового баланса
c = a + b  # можем складывать экземпляры
e = b + a  # сохранится имя того экземпляра, который будет первым
print(d)
print(c)
print(e)
