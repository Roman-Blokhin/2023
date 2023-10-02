# Геттеры и сеттеры, property атрибуты

class BankAccount:

    def __init__(self, name, balance):  # создали защищенные данные баланса, которые напрямую не вывести
        self.name = name
        self.__balance = balance

    def get_balance(self):  # создали функцию, которая выводит защищенные данные через метод
        return self.__balance

    def set_balance(self, value):  # создали функцию, которая присваивает новое значение защищенным данным через метод
        self.__balance = value

a = BankAccount("Roman", 100)