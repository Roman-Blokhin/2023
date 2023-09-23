# СОЗДАЕМ СПИСОК И ПРОВЕРЯЕМ, ЕСТЬ ЛИ В НЕМ ОПРЕДЕЛЕННОЕ ЧИСЛО

list = [1, 8, 9, 56, 903, 578, 80, 46, 234, 5, 0, -4]

for i in list:
    if i == 9:
        print('YES')
    else:
        print('no')

print()

# СОЗДАЕМ ДВУМЕРНЫЙ МАССИВ С РАНДОМНЫМИ ЧИСЛАМИ И ПРОВЕРЯЕМ, ЕСТЬ ЛИ В НЕМ НУЖНОЕ ЧИСЛО

import random as r

n = 5
m = 7
mas = [[0 for i in range(m)] for j in range(n)] # создаем массив, столбцы и строки, присваивая объектам значение 0

for i in range(n): # создаем условие, которое присваивает всем объектам в массиве рандомное число
    for j in range(m):
        mas[i][j] = r.randint(0, 9)

for i in range(n): # перебираем все объекты в строчке для вывода
    for j in range(m): # перебираем все объекты в колонке для вывода
        print(mas[i][j], end=' ')
    print()

for i in range(n): # создаем условие, которое присваивает значение 20 всем объектам на главной диагонали
    for j in range(m):
        if i == j:
            mas[i][j] = 20
print()

for i in range(n): # выводим уже новую матрицу с обновленными значениями
    for j in range(m):
        print(mas[i][j], end=' ')
    print()

# получаем сумму чисел в массиве
s = 0
for i in range(n):
    for j in range(m):
        s += mas[i][j] # складываем все числа в массиве
print (s)

# заменяем числа, которые делятся на число 7 без остатка на значок амперсанда
for i in range(n):
    for j in range(m):
        if mas[i][j] % 7 == 0:
            mas[i][j] = "&"

print ()

for i in range(n): # выводим уже новую матрицу с обновленными значениями амперсанда
    for j in range(m):
        print(mas[i][j], end=' ')
    print()





