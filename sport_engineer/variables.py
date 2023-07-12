from colorama import Fore, Back, Style

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
