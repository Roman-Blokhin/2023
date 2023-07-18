# ХОЧУ НАПИСАТЬ ПРОГРАММУ, КОТОРАЯ БУДЕТ ВЫВОДИТЬ ТРЕНИРОВКИ ДЛЯ ОПРЕДЕЛЕННОЙ ГРУППЫ МЫШЦ В ОПРЕДЕЛЕННЫЙ ДЕНЬ С ВИЗУАЛОМ

import tkinter as tk
from tkinter import *
from variables import *

# ---------------------- 1. Создаем основное окно -----------------------

root = Tk ()
root.title ('Система тренировок')
root.geometry ('750x700+50+50')
root.config (bg = 'DarkGrey')

# ---------------------- 3. Создаем кнопки и лейблы -----------------------

tk.Button (root, text="Готовая тренировка", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="black",).\
    grid(row=1, column=0, sticky="we", padx=7, pady=7)

tk.Button (root, text="Выбрать схему упражнений", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="black").\
    grid(row=2, column=0, sticky="we", padx=7, pady=7)

tk.Button (root, text="Обратная связь", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="black").\
    grid(row=3, column=0, sticky="we", padx=7, pady=7)

tk.Label (root, text=" ").grid(row=4, column=0)
tk.Label (root, text=" ").grid(row=5, column=0)
tk.Label (root, text=" ").grid(row=6, column=0)
tk.Label (root, text=" ").grid(row=7, column=0)
tk.Label (root, text=" ").grid(row=8, column=0)
tk.Label (root, text=" ").grid(row=9, column=0)
tk.Label (root, text=" ").grid(row=10, column=0)
tk.Label (root, text=" ").grid(row=11, column=0)
tk.Label (root, text=" ").grid(row=12, column=0)
tk.Label (root, text=" ").grid(row=13, column=0)

# ---------------------- 4. Создаем окно для вывода информации -----------------------

win = tk.Text(root, width=30, height=20, bg="white", font=("Arial", 14, "normal"))
win.grid(row=1, column=3, rowspan=13)

# ---------------------- 5. Присваиваем размер нашим строкам и столбцам -----------------------

root.grid_columnconfigure(0, minsize=50)
root.grid_columnconfigure(1, minsize=50)
root.grid_columnconfigure(2, minsize=50)
root.grid_columnconfigure(3, minsize=50)

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