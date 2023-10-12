# Замыкания часть 2
# создаем функцию, которая будет подсчитывать среднее значение

def average_numbers():
    number = []  # создаем пустой список

    def inner(num):
        number.append(num)  # добавляем новый аргумент в список
        print(number)
        return sum(number) / len(number)  # возвращаем среднее значение от суммы чисел

    return inner

