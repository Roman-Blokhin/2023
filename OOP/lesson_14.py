# Classmethod и staticmethod

class Example:
    def hello():  # 1. мы не можем вывести через экземпляр, но можем через класс - Example.hello()
        print('hello')

    def instance_hello(self):  # 2. мы не можем вывести через сам класс, но можем через экземпляр - q.instance_hello()
        print(f'instance_hello + {self}')

    @staticmethod  # 3. навешиваем декоратор
    def static_hello():  # 3.1 можем вывести и через сам класс, и через экземпляр класса
        print('static_hello')


Example.hello()  # 1.1 можем вызвать через класс

q = Example()  # присваиваем экземпляр классу
q.instance_hello()  # 2.1 можем вызвать через экземпляр

# 3.2 с помощью декоратора @staticmethod, можем вывести и через сам класс, и через экземпляр класса
w = Example()
Example.static_hello()
w.static_hello()
