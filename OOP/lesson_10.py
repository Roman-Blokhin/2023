# Геттеры и сеттеры, property атрибуты

class BankAccount:

    def __init__(self, name, balance):  # создали защищенные данные баланса, которые напрямую не вывести
        self.name = name
        self.__balance = balance

    def get_balance(self):  # создали функцию, которая выводит защищенные данные через метод
        return self.__balance

    def set_balance(self, value):  # создали функцию, которая присваивает новое значение защищенным данным через метод
        if not isinstance(value, (int, float)):  # прописываем условие, чтобы наше значение было числом
            raise ValueError ('Баланс должен быть числом')  # если будет не числом, то выведется ошибка
        self.__balance = value

a = BankAccount("Roman", 100)

print(a.__dict__)  # смотрим атрибуты экземпляра
print(a._BankAccount__balance)  # копируем из атрибутов экземпляра зашифрованный атрибут и выводим, не напрямую

b = BankAccount('Ilon', 400)
print(b.__dict__)
print(b._BankAccount__balance)

b.get_balance()  # используем метод косвенного вывода защищенного атрибута
b.set_balance('hello')  # переопределяем значение защищенного атрибута с помощью метода
print(b._BankAccount__balance)
