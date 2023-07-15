# ХОЧУ НАПИСАТЬ ПРОГРАММУ, КОТОРАЯ БУДЕТ ВЫВОДИТЬ ТРЕНИРОВКИ ДЛЯ ОПРЕДЕЛЕННОЙ ГРУППЫ МЫШЦ В ОПРЕДЕЛЕННЫЙ ДЕНЬ С ВИЗУАЛОМ

import tkinter as tk
from tkinter import *

def monday():
    tk.Label (root, text="Ноги + Плечи", font=("Arial", 20, "bold"), fg="red", bg="grey").\
        grid(row=3, column=0, columnspan=3)
    win.insert (tk.END, ', здравствуйте')

# ---------------------- 1. Создаем основное окно -----------------------

root = Tk ()
root.title ('Система тренировок')
root.geometry ('900x700+50+50')
root.config (bg = 'grey')

# ---------------------- 3. Создаем кнопки и лейблы -----------------------

tk.Label(root, text=" ", bg="grey").grid(row=0, column=0)

tk.Label(root, text="Выберите день тренировки:", bg="grey", font=("Arial", 16, "bold"), fg="white").\
    grid(row=1, column=0, columnspan=3, stick="we")

tk.Button(root, text="Понедельник", bg="grey", font=("Arial", 12, "bold"), fg="white", command=monday).\
    grid(row=2, column=0, stick="we", padx=7, pady=7)
tk.Button(root, text="Среда", bg="grey", font=("Arial", 12, "bold"), fg="white").\
    grid(row=2, column=1, stick="we", padx=7, pady=7)
tk.Button(root, text="Пятница", bg="grey", font=("Arial", 12, "bold"), fg="white").\
    grid(row=2, column=2, stick="we", padx=7, pady=7)

# ---------------------- 4. Создаем окно для вывода информации -----------------------

win = tk.Text(root, width=50, height=30, bg="white", font=("Arial", 16, "normal"))
win.grid(row=1, column=3, rowspan=16)

# ---------------------- 5. Присваиваем размер нашим строкам и столбцам -----------------------

root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=150)
root.grid_columnconfigure(2, minsize=150)
root.grid_columnconfigure(3, minsize=150)

root.grid_rowconfigure(0, minsize=20)
root.grid_rowconfigure(1, minsize=10)
root.grid_rowconfigure(2, minsize=10)
root.grid_rowconfigure(3, minsize=20)

# ---------------------- 2. Закрываем программу -----------------------

root.mainloop ()

# --------------- TO-DO -----------------

# написать визуал программы с выводом информации на экран
# возможность выбрать по отдельности часть тела для выдачи в результате упражнений