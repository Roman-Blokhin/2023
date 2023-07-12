# ХОЧУ НАПИСАТЬ ПРОГРАММУ, КОТОРАЯ БУДЕТ ВЫВОДИТЬ СПИСОК УПРАЖНЕНИЙ ДЛЯ ОПРЕДЕЛЕННОЙ ГРУППЫ МЫШЦ В ОПРЕДЕЛЕННЫЙ ДЕНЬ

from colorama import Fore, Back, Style

while True:
    choice_workout = (Fore.BLUE + "\nВыберите схему тренировок: " + Style.RESET_ALL)
    choice_day = (Fore.GREEN + "\nВыбрать день недели: " + Style.RESET_ALL)

    sh_1 = "\nСхема тренировок №1"
    sh_2 = "\nСхема тренировок №2"

    var_1 = "\n1. Вариант 1"
    var_2 = "\n2. Вариант 2"

    mo = (Fore.YELLOW + "\n1. Понедельник" + Style.RESET_ALL)
    we = (Fore.YELLOW + "\n2. Среда" + Style.RESET_ALL)
    fr = (Fore.YELLOW + "\n3. Пятница" + Style.RESET_ALL)
    ex = (Fore.YELLOW + "\n4. Выход" + Style.RESET_ALL)

    legs_shoulders = (Fore.RED + "\nНоги + Плечи" + Style.RESET_ALL)
    chest_biceps = (Fore.RED + "\nГрудь + Бицепс" + Style.RESET_ALL)
    back_triceps = (Fore.RED + "\nСпина + Трицепс" + Style.RESET_ALL)

    game_over = (Fore.BLUE + "\nДо свидания. Хорошей тренировки!" + Style.RESET_ALL)

    back = (Fore.RED + "\nДля продолжения нажмите: " + Style.RESET_ALL) + "Enter" + \
           (Fore.RED + ", для выхода: " + Style.RESET_ALL) + "9"

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

# сделать подсветку текста цветом
# прописать ошибки и исключения
# добавить схему тренировок
# прописать разминочные и заминочные упражнения
# подключить файл для записи системы тренировок
# понять, как подключать файлы питона друг к другу

# возможность выбрать по отдельности часть тела для выдачи в результате упражнений