# ХОЧУ НАПИСАТЬ ПРОГРАММУ, КОТОРАЯ БУДЕТ ВЫВОДИТЬ СПИСОК УПРАЖНЕНИЙ ДЛЯ ОПРЕДЕЛЕННОЙ ГРУППЫ МЫШЦ В ОПРЕДЕЛЕННЫЙ ДЕНЬ

while True:
    choice_workout = "\nВыберите схему тренировок: "
    choice_day = "\nВыбрать день недели: "

    sh_1 = "\nСхема тренировок №1"
    sh_2 = "\nСхема тренировок №2"

    var_1 = "\n1. Вариант 1"
    var_2 = "\n2. Вариант 2"

    mo = "\n1. Понедельник"
    we = "\n2. Среда"
    fr = "\n3. Пятница"
    ex = "\n4. Выход"

    legs_shoulders = "\nНоги + Плечи"
    chest_biceps = "\nГрудь + Бицепс"
    back_triceps = "\nСпина + Трицепс"

    game_over = "\nДо свидания. Хорошей тренировки!"

    back = "\nДля продолжения нажмите: Enter, для выхода: 9 "

    print(mo, we, fr, ex)

    choice_1_level = input(choice_day)

    if choice_1_level == "1":
        print(legs_shoulders)
        print(var_1, var_2)
        choice_2_level = input(choice_workout)
        if choice_2_level == "1":
            print(sh_1)
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

# возможность выбрать по отдельности часть тела для выдачи в результате упражнений