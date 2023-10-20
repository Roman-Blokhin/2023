# Декоратор Property (Property decorator)

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property  # 1. создаем декоратор свойства геттер
    def my_balance(self):  # 2. меняем название функции на my_balance, потому что функция задекорирована
        print('get balance')
        return self.__balance

    @my_balance.setter  # 3. декорируем сеттер, но вызываем его как свойство, чтобы не было совпадения имен
    def my_balance(self, value):  # 4. меняем название, потому что задекорирована функция
        if not isinstance(value, (int, float)):
            raise ValueError ('Баланс должен быть числом')
        print('set balance')
        self.__balance = value

    @my_balance.deleter  # 5. декорируем делитер
    def my_balance(self):  # 6. меняем название, потому что задекорирована функция
        print('delete balance')
        del self.__balance

    # меняем запись свойства, делаем удобней
#    my_balance = property(get_balance)
#    # my_balance = my_balance.getter(get_balance)  # геттер может принимать сразу наше свойство  my_balance
#    my_balance = my_balance.setter(set_balance)
#    my_balance = my_balance.deleter(delete_balance)




