# Публичные, приватные, защищенные атрибуты и методы

class BankAccount:

    def __init__(self, name, balance, passport):
        # self.name = name  # публичные данные
        # self.balance = balance # публичные данные
        # self.passport = passport # публичные данные
        self.__name = name  # защищенные данные
        self.__balance = balance  # защищенные данные
        self.__passport = passport  # защищенные данные

    # def print_public_data(self): # создали публичную функцию, которая выводит данные как внутри банка, так и вне банка
    #     print(self.name, self.balance, self.passport)

    # на уровне согласования между разработчиками временно ставится protected - данные с нижним подчеркиванием впереди
    # def print_protected_data(self): # публичная функция, которая выводит данные как внутри банка, так и вне банка
    #     print(self._name, self._balance, self._passport)

    # создаем приватные (защищенные) - private данные, которые можно вызвать только через функцию
    # напрямую к данным обратиться нельзя, мы их ИНКАПСУЛИРУЕМ - СКРЫВАЕМ
    # можно обратиться только внутри класса через публичную функцию, где будет обращение к приватной функции
    def print_private_data(self):  # публичная функция, которая выводит данные как внутри банка, так и вне банка
        print(self.__name, self.__balance, self.__passport)

    def print_def(self):
        self.print_private_data()


account_1 = BankAccount('Roman', 1000, 5670987)
account_1.print_private_data()
# print(account_1._name)   # данные protected, но это всего лишь для согласования с разработчиками
# print(account_1._balance)
# print(account_1._passport)

account_1.print_def()  # так мы обращаемся к защищенным данным не напрямую, а внутри класса

print(account_1.__name)  # будет ошибка, если обратиться к приватным данным напрямую
