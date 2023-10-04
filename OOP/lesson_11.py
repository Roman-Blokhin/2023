# Декоратор Property (Property decorator)

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance')
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError ('Баланс должен быть числом')
        print('set balance')
        self.__balance = value

    def delete_balance(self):
        print('delete balance')
        del self.__balance

    # меняем запись свойства, делаем удобней
    my_balance = property(get_balance)
    # my_balance = my_balance.getter(get_balance)  # геттер может принимать сразу наше свойство  my_balance
    my_balance = my_balance.setter(set_balance)
    my_balance = my_balance.deleter(delete_balance)




