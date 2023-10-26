# Classmethod и staticmethod

class Example:
    def hello():  # 1. мы не можем вывести через экземпляр, но можем через класс - Example.hello()
        print('hello')

    def instance_hello(self):  # 2. мы не можем вывести через сам класс, но можем через экземпляр - q.instance_hello()
        print('instance_hello')


Example.hello()  # 1.1 можем вызвать через класс

q = Example()  # присваиваем экземпляр классу
q.instance_hello()  # 2.1 можем вызвать через экземпляр
