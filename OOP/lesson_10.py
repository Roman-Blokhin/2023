# Геттеры и сеттеры, property атрибуты

class BankAccount:

    def __init__(self, name, balance):  # создали защищенные данные баланса, которые напрямую не вывести
        self.name = name
        self.__balance = balance

    def get_balance(self):  # создали функцию, которая выводит защищенные данные через метод
        print('get balance')
        # проверка, есть ли деньги на балансе, если сработала, то баланс потом не переопределить
        # if not isinstance(self, (int, float)):
        #     print('У вас нет денег')
        return self.__balance

    def set_balance(self, value):  # создали функцию, которая присваивает новое значение защищенным данным через метод
        if not isinstance(value, (int, float)):  # прописываем условие, чтобы наше значение было числом
            raise ValueError ('Баланс должен быть числом')  # если будет не числом, то выведется ошибка
        print('set balance')
        self.__balance = value

    def delete_balance(self):  # метод удаления значения свойства
        print('delete balance')
        del self.__balance

    # создаем свойство, чтобы заменить название методов для упрощения кода
    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)

a = BankAccount("Roman", 100)

print(a.__dict__)  # смотрим атрибуты экземпляра
print(a._BankAccount__balance)  # копируем из атрибутов экземпляра зашифрованный атрибут и выводим, не напрямую

b = BankAccount('Ilon', 400)
print(b.__dict__)
print(b._BankAccount__balance)

b.get_balance()  # используем метод косвенного вывода защищенного атрибута
b.set_balance(500)  # переопределяем значение защищенного атрибута с помощью метода
print(b._BankAccount__balance)

c = BankAccount('Mark', 700)
print (c.balance)  # выводим значение с помощью метода get_balance, через свойство
c.balance = 800  # переопределяем значение с помощью метода set_balance, через свойство
print (c.balance)
del c.balance  # удалили наше значение баланса через свойство и метод delete_balance
c.balance = 900  # снова переопределили наше значение приватного атрибута - баланс, через свойство
print(c.balance)


