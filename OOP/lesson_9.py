# Публичные, приватные, защищенные атрибуты и методы

class BankAccount:

    def __init__(self, name, balance, passport):
        # self.name = name  # публичные данные
        # self.balance = balance # публичные данные
        # self.passport = passport # публичные данные
        self._name = name  # защищенные данные
        self._balance = balance # защищенные данные
        self._passport = passport # защищенные данные

    # def print_public_data(self): # создали публичную функцию, которая выводит данные как внутри банка, так и вне банка
    #     print(self.name, self.balance, self.passport)

    # на  уровне согласования между разработчиками временно ставится protected - данные с нижним подчеркиванием впереди
    def print_protected_data(self): # создали публичную функцию, которая выводит данные как внутри банка,
        # так и вне банка
        print(self._name, self._balance, self._passport)

account_1 = BankAccount('Roman', 1000, 5670987)
account_1.print_protected_data()
