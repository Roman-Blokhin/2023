# Публичные, приватные, защищенные атрибуты и методы

class BankAccount:

    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_public_data(self): # создали публичную функцию, которая выводит данные как внутри банка, так и вне банка
        print(self.name, self.balance, self.passport)

account_1 = BankAccount('Roman', 1000, 5670987)
account_1.print_public_data()
