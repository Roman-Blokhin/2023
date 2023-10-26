# Classmethod и staticmethod

class Example:
    def hello():  # 1. мы не можем вывести через экземпляр, но можем через класс - Example.hello()
        print('hello')

    def instance_hello(self):  # 2. мы не можем вывести через сам класс, но можем через экземпляр - q.instance_hello()
        print(f'instance_hello + {self}')

    @staticmethod  # 3. навешиваем декоратор, помогает не обращать внимание на способ вызова функции
    def static_hello():  # 3.1 можем вывести и через сам класс, и через экземпляр класса
        print('static_hello')

    @classmethod  # 4. декоратор, помогает когда нужна обработка целого класса
    def class_hello(cls):  # 4.1 обращаемся к классу, а не к методу, аргумент специализирован
        print(f'class_hello + {cls}')


Example.hello()  # 1.1 можем вызвать через класс

q = Example()  # присваиваем экземпляр классу
q.instance_hello()  # 2.1 можем вызвать через экземпляр

# 3.2 с помощью декоратора @staticmethod, можем вывести и через сам класс, и через экземпляр класса
w = Example()
Example.static_hello()
w.static_hello()

# 4. с помощью декоратора @classmethod мы обращаем не к экземпляру, а всегда к целому классу
s = Example()
Example.class_hello()
s.class_hello()

# можно узнать, к какому классу принадлежит экземпляр
print('Экземпляр s принадлежит к классу:', s.__class__)
