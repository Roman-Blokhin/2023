# НАЧИНАЮ ИЗУЧЕНИЕ ООП С НУЛЯ, С САМЫХ АЗОВ

class Car:
    model = None
    cost = 0

car_1 = Car() # присвоил экземпляр классу Car
car_1.cost = 15000 # задаем параметры для нашего экземпляра
car_1.model = 'BMW'

car_2 = Car()
car_2.color = 'red'

print (car_1.cost)
print (car_2.color)