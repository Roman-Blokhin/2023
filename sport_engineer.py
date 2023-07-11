# ХОЧУ НАПИСАТЬ ПРОГРАММУ, КОТОРАЯ БУДЕТ ВЫВОДИТЬ СПИСОК УПРАЖНЕНИЙ ДЛЯ ОПРЕДЕЛЕННОЙ ГРУППЫ МЫШЦ В ОПРЕДЕЛЕННЫЙ ДЕНЬ

choice_workout = "\nВыберите схему тренировок: "
choice_day = "\nВыбрать день недели: "

sh_1 = "\nСхема тренировок №1"
sh_2 = "\nСхема тренировок №2"

var_1 = "\n1. Вариант 1"
var_2 = "\n2. Вариант 2"

mo = "\n1. Понедельник"
we = "\n2. Среда"
fr = "\n3. Пятница"

legs_shoulders = "\nНоги + Плечи"
chest_biceps = "\nГрудь + Бицепс"
back_triceps = "\nСпина + Трицепс"

print(mo, we, fr)

a = input(choice_day)

if a == "1":
    print(legs_shoulders)
    print(var_1, var_2)
    b = input(choice_workout)
    if b == "1":
        print(sh_1)
    else:
        print(sh_2)

if a == "2":
    print(chest_biceps)
    print(var_1, var_2)
    b = input(choice_workout)
    if b == "1":
        print(sh_1)
    else:
        print(sh_2)

if a == "3":
    print(back_triceps)
    print(var_1, var_2)
    b = input(choice_workout)
    if b == "1":
        print(sh_1)
    else:
        print(sh_2)

# возможность выбрать по отдельности часть тела для выдачи в результате упражнений