# ХОЧУ НАПИСАТЬ ПРОГРАММУ, КОТОРАЯ БУДЕТ ВЫВОДИТЬ ТРЕНИРОВКИ ДЛЯ ОПРЕДЕЛЕННОЙ ГРУППЫ МЫШЦ В ОПРЕДЕЛЕННЫЙ ДЕНЬ С ВИЗУАЛОМ

import tkinter as tk
from tkinter import *
from variables import *

# def monday():
#     print("Monday")
#     tk.Label (root, text="Выбери этапы тренировки:", font=("Arial", 16, "bold"), fg="red", bg="Seashell").\
#         grid(row=3, column=0, columnspan=3)
#
#     tk.Checkbutton ()
#
#     tk.Label (root, text="Ноги + Плечи", font=("Arial", 16, "bold"), fg="red", bg="Gainsboro").\
#         grid(row=4, column=0, columnspan=3)
#     win.insert (tk.END, legs_1)
#
# def finish_sport ():
#     # tk.Label(root, text=" ", bg="grey").grid(row=0, column=0)
#
#     tk.Label(root, text="Выберите день тренировки:", bg="grey", font=("Arial", 18, "bold"), fg="white").\
#         grid(row=1, column=0, columnspan=3, sticky="we", rowspan=2, padx=40, pady=40)
#
#     tk.Checkbutton(root, text="Понедельник", bg="grey", font=("Arial", 12, "bold"), fg="white", indicatoron=0,
#                    command=monday).grid(row=2, column=0, stick="we", padx=7, pady=7)
#     tk.Checkbutton(root, text="Среда", bg="grey", font=("Arial", 12, "bold"), fg="white", indicatoron=0).\
#         grid(row=2, column=1, stick="we", padx=7, pady=7)
#     tk.Checkbutton(root, text="Пятница", bg="grey", font=("Arial", 12, "bold"), fg="white", indicatoron=0).\
#         grid(row=2, column=2, stick="we", padx=7, pady=7)

# ---------------------- 1. Создаем основное окно -----------------------

root = Tk ()
root.title ('Система тренировок')
root.geometry ('950x700+50+50')
root.config (bg = 'DarkGrey')

# ---------------------- 3. Создаем кнопки и лейблы -----------------------

tk.Button (root, text="Готовая тренировка", bg="LightGrey", font=("Comic Sans MS", 16, "normal"), fg="black",
           command=finish_sport).grid(row=1, column=0, columnspan=3, sticky="we", padx=40, pady=40)

tk.Button (root, text="Выбрать схему упражнений", bg="LightGrey", font=("Comic Sans MS", 16, "normal"), fg="black").\
    grid(row=2, column=0, columnspan=3, sticky="we", padx=40, pady=40)

tk.Button (root, text="Обратная связь", bg="LightGrey", font=("Comic Sans MS", 16, "normal"), fg="black").\
    grid(row=3, column=0, columnspan=3, sticky="we", padx=40, pady=40)

# ---------------------- 4. Создаем окно для вывода информации -----------------------

win = tk.Text(root, width=40, height=27, bg="white", font=("Arial", 16, "normal"))
win.grid(row=1, column=3, rowspan=16)

# ---------------------- 5. Присваиваем размер нашим строкам и столбцам -----------------------

root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=150)
root.grid_columnconfigure(2, minsize=150)
root.grid_columnconfigure(3, minsize=150)

root.grid_rowconfigure(0, minsize=20)
root.grid_rowconfigure(1, minsize=20)
root.grid_rowconfigure(2, minsize=20)
root.grid_rowconfigure(3, minsize=20)
root.grid_rowconfigure(4, minsize=20)
root.grid_rowconfigure(5, minsize=20)

# ---------------------- 2. Закрываем программу -----------------------

root.mainloop ()

# --------------- TO-DO -----------------

# написать визуал программы с выводом информации на экран
# возможность выбрать по отдельности часть тела для выдачи в результате упражнений