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

q = BankAccount('oi', 100)
w = BankAccount('oi', 1)
print(q+w)  # можно менять местами элементы при сложении, если это экземпляры класса, а не экземпляр + новое знач.
print(w+q)

r = BankAccount('aa', 1)  # с помощью __radd__ мы можем менять слагаемые местами без ошибки
print(12 + r)