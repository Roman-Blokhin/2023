# ПРАКТИКА С property

from string import digits  # импортируем digits - все числа 0-9, записанные строкой

file = open("pass.txt", "r", encoding="utf-8")  # открываем текстовый файл с паролями, который лежит в этой же папке
content = file.read()  # создаем переменную в которую вкладываем все содержимое файла


class User:
    def __init__(self, login, password):
        self.__login = login
        self.password = password  # мы заменяем __password на свойство password, чтобы все проверки подключились
        self.__secret = 'В сундуке лежит 10 золотых'  # новая проверка

    @property  # мы создали еще одну проверку для входа куда-либо, где нужно вводить пароль
    def secret(self):
        s = input('Введите пароль: ')
        if s == self.password:
            print(self.__secret)
        else:
            raise ValueError('Доступ закрыт')

    @property
    def password(self):
        return self.__password

    @staticmethod  # чтобы self не применялся, вешаем декоратор (не вызывает экземпляр класса)
    def is_include_number(password):
        for i in digits:  # пробегаемся по нашему паролю, если там есть цифра - True
            if i in password:
                return True

        return False  # если в цикле цифры нет, возвращаем False

    @staticmethod  # создаем метод, который проверяет, есть ли строчка(наш пароль) в списке подключенного файла
    def is_pass(value):
        position = content.find(value)
        if position != -1:
            return False

        return True

    @password.setter
    def password(self, value):
        if not isinstance(value, str):  # проверяет наш пароль, является ли он строкой
            raise TypeError('Пароль должен быть текстом')
        if len(value) < 4:  # проверяет пароль на минимальное количество символов
            raise ValueError('Длина пароль не может быть меньше 4 символов')
        if len(value) > 10:  # проверяет пароль на максимальное количество символов
            raise ValueError('Длина пароль не может быть больше 10 символов')
        if not User.is_include_number(value):  # проверка, содержится ли в новом пароле хотя бы одна цифра
            raise ValueError('Пароль должен содержать хоть одну цифру')
        if not self.is_pass(value): # проверка, содержит ли наш пароль текст из файла с паролями - можно self. или User.
            raise ValueError('Легкий пароль')
        self.__password = value

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        self.__login = value

# ------------------------ #
# ПОДКЛЮЧАЕМ ФАЙЛ С ПАРОЛЯМИ, ЧТОБЫ ПРОВЕРИТЬ, ЕСТЬ ЛИ ТАМ НАБРАННЫЙ ПОЛЬЗОВАТЕЛЕМ ПАРОЛЬ

a = User('roman', 'QWERTYj2')  # создаем экземпляр со значениями
a.password = 'QWERT2'  # присваиваем новое значение паролю
print(a.password)

