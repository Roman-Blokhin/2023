# ХОЧУ НАПИСАТЬ ПРОГРАММУ, КОТОРАЯ БУДЕТ ВЫВОДИТЬ СПИСОК УПРАЖНЕНИЙ ДЛЯ ОПРЕДЕЛЕННОЙ ГРУППЫ МЫШЦ В ОПРЕДЕЛЕННЫЙ ДЕНЬ

from variables import * # мы подключили файл variables.py, куда перенесли все переменные

while True:
    print(mo, we, fr, ex)
    choice_1_level = input(choice_day) # 1 уровень - выберите день недели

    if choice_1_level == "1":
        print(legs_shoulders)
        print(var_1, var_2)
        choice_2_level = input(choice_workout) # 2 уровень - выберите схему тренировок
        if choice_2_level == "1":
            print(sh_1) # сама схема тренировок
        else:
            print(sh_2)

    if choice_1_level == "2":
        print(chest_biceps)
        print(var_1, var_2)
        choice_2_level = input(choice_workout)
        if choice_2_level == "1":
            print(sh_1)
        else:
            print(sh_2)

    if choice_1_level == "3":
        print(back_triceps)
        print(var_1, var_2)
        choice_2_level = input(choice_workout)
        if choice_2_level == "1":
            print(sh_1)
        else:
            print(sh_2)

    if choice_1_level == "4":
        print(game_over)
        break

    come_back = input (back)

    if come_back == "9":
        print(game_over)
        break

# прописать ошибки и исключения
# добавить схему тренировок
# прописать разминочные и заминочные упражнения
# подключить файл для записи системы тренировок
# понять, как подключать файлы питона друг к другу

# возможность выбрать по отдельности часть тела для выдачи в результате упражнений