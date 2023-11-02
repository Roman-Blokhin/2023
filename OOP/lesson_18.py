# Магические методы __add__, __mul__, __sub__ и __truediv__
# отвечают за базовые математические операции

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):  # сложение, нужен второй аргумент, первый - наш клиент, второй - новый баланс
        print('__add__ был вызван')
        if isinstance(other, (int, float)):  # если значение принадлежит к типам int или float
            return self.balance + other