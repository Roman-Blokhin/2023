# ХОЧУ НАПИСАТЬ ПРОГРАММУ, КОТОРАЯ БУДЕТ ВЫВОДИТЬ ТРЕНИРОВКИ ДЛЯ ОПРЕДЕЛЕННОЙ ГРУППЫ МЫШЦ В ОПРЕДЕЛЕННЫЙ ДЕНЬ С ВИЗУАЛОМ

import tkinter as tk
from tkinter import *
from variables import *

# ---------------------- 6. Создаем функции -----------------------

def programs (): # функция для выбора готовой тренировки
    # ---------------------------------------- Грудь + Бицепс
    # я поместил функцию создания кнопок в функцию нажатия на кнопку - грудь+бицепс, блокируя ее
    def start_b_b ():
        # кнопка 1 тренировки на: грудь + бицепс
        btn_1_1 = tk.Button (root, text="1", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="red",
                         state="normal", command=program_1_1)
        btn_1_1.grid(row=2, column=1, sticky="we", padx=7, pady=7)

        # кнопка 2 тренировки на: грудь + бицепс
        btn_1_2 = tk.Button (root, text="2", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="red",
                         state="normal", command=program_1_2)
        btn_1_2.grid(row=2, column=2, sticky="we", padx=7, pady=7)

        # кнопка 3 тренировки на: грудь + бицепс
        btn_1_3 = tk.Button (root, text="3", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="red",
                         state="normal", command=program_1_3)
        btn_1_3.grid(row=2, column=3, sticky="we", padx=7, pady=7)

        # кнопка блокировки кнопки - грудь+бицепс и разблокировка остальных
        btn_1.config(state='disabled')
        btn_2.config(state='normal')
        btn_3.config(state='normal')

        # создаем лейблы, которые скроют нам ненужные кнопки у неактивных систем тренировок
        l_1 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_1.grid(row=3, column=1, sticky="we", padx=7, pady=7)

        l_2 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_2.grid(row=3, column=2, sticky="we", padx=7, pady=7)

        l_3 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_3.grid(row=3, column=3, sticky="we", padx=7, pady=7)

        l_4 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_4.grid(row=4, column=1, sticky="we", padx=7, pady=7)

        l_5 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_5.grid(row=4, column=2, sticky="we", padx=7, pady=7)

        l_6 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_6.grid(row=4, column=3, sticky="we", padx=7, pady=7)

    # кнопка "Грудь + Бицепс", которая создает другие кнопки с вариантами тренировок
    btn_1 = tk.Button (root, text="Грудь + Бицепс", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="red",
               state="normal", command=start_b_b)
    btn_1.grid(row=2, column=0, sticky="we", padx=7, pady=7)

    # ------------------------------------- Спина + Трицепс
    def start_b_t ():
        btn_2_1 = tk.Button (root, text="1", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="red",
                             state="normal", command=program_2_1)
        btn_2_1.grid(row=3, column=1, sticky="we", padx=7, pady=7)

        btn_2_2 = tk.Button (root, text="2", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="red",
                             state="normal", command=program_2_2)
        btn_2_2.grid(row=3, column=2, sticky="we", padx=7, pady=7)

        btn_2_3 = tk.Button (root, text="3", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="red",
                             state="normal", command=program_2_3)
        btn_2_3.grid(row=3, column=3, sticky="we", padx=7, pady=7)

        # кнопка блокировки кнопки - спина+трицепс и разблокировка остальных
        btn_2.config(state='disabled')
        btn_1.config(state='normal')
        btn_3.config(state='normal')

        # создаем лейблы, которые скроют нам ненужные кнопки у неактивных систем тренировок
        l_1 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_1.grid(row=2, column=1, sticky="we", padx=7, pady=7)

        l_2 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_2.grid(row=2, column=2, sticky="we", padx=7, pady=7)

        l_3 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_3.grid(row=2, column=3, sticky="we", padx=7, pady=7)

        l_4 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_4.grid(row=4, column=1, sticky="we", padx=7, pady=7)

        l_5 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_5.grid(row=4, column=2, sticky="we", padx=7, pady=7)

        l_6 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_6.grid(row=4, column=3, sticky="we", padx=7, pady=7)

    btn_2 = tk.Button (root, text="Спина + Трицепс", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="red",
                       command=start_b_t)
    btn_2.grid(row=3, column=0, sticky="we", padx=7, pady=7)

    # ------------------------------------------------- Ноги + Плечи
    def start_l_b ():
        btn_3_1 = tk.Button (root, text="1", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="red",
                             state="normal", command=program_3_1)
        btn_3_1.grid(row=4, column=1, sticky="we", padx=7, pady=7)

        btn_3_2 = tk.Button (root, text="2", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="red",
                             state="normal", command=program_3_2)
        btn_3_2.grid(row=4, column=2, sticky="we", padx=7, pady=7)

        btn_3_3 = tk.Button (root, text="3", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="red",
                             state="normal", command=program_3_3)
        btn_3_3.grid(row=4, column=3, sticky="we", padx=7, pady=7)

        # кнопка блокировки кнопки - ноги + плечи и разблокировка остальных
        btn_3.config(state='disabled')
        btn_2.config(state='normal')
        btn_1.config(state='normal')

        # создаем лейблы, которые скроют нам ненужные кнопки у неактивных систем тренировок
        l_1 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_1.grid(row=3, column=1, sticky="we", padx=7, pady=7)

        l_2 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_2.grid(row=3, column=2, sticky="we", padx=7, pady=7)

        l_3 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_3.grid(row=3, column=3, sticky="we", padx=7, pady=7)

        l_4 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_4.grid(row=2, column=1, sticky="we", padx=7, pady=7)

        l_5 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_5.grid(row=2, column=2, sticky="we", padx=7, pady=7)

        l_6 = tk.Label (root, text=" ", bg="DarkGrey", font=("Comic Sans MS", 19, "normal"))
        l_6.grid(row=2, column=3, sticky="we", padx=7, pady=7)

    btn_3 = tk.Button (root, text="Ноги + Плечи", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="red",
                       command=start_l_b)
    btn_3.grid(row=4, column=0, sticky="we", padx=7, pady=7)

# ------------------------------ Тренировки на Грудь + Бицепс - 3 варианта -----------------------------

def program_1_1 (): # выводим тренировку: грудь + бицепс в окно - 1 неделя
    win.delete ('1.0', tk.END)
    win.insert (tk.END, chest_biceps_1)

def program_1_2 (): # выводим тренировку: грудь + бицепс в окно - 2 неделя
    win.delete ('1.0', tk.END)
    win.insert (tk.END, chest_biceps_2)

def program_1_3 (): # выводим тренировку: грудь + бицепс в окно - 3 неделя
    win.delete ('1.0', tk.END)
    win.insert (tk.END, chest_biceps_3)

# ------------------------------ Тренировки на Спина + Трицепс - 3 варианта -----------------------------

def program_2_1 (): # выводим тренировку: спина + трицепс в окно - 1 неделя
    win.delete ('1.0', tk.END)
    win.insert (tk.END, back_triceps_1)

def program_2_2 (): # выводим тренировку: спина + трицепс в окно - 2 неделя
    win.delete ('1.0', tk.END)
    win.insert (tk.END, back_triceps_2)

def program_2_3 (): # выводим тренировку: спина + трицепс в окно - 3 неделя
    win.delete ('1.0', tk.END)
    win.insert (tk.END, back_triceps_3)

# ------------------------------ Тренировки на Ноги + Плечи - 3 варианта -----------------------------

def program_3_1 (): # выводим тренировку: ноги + плечи в окно - 1 неделя
    win.delete ('1.0', tk.END)
    win.insert (tk.END, legs_shoulders_1)

def program_3_2 (): # выводим тренировку: ноги + плечи в окно - 2 неделя
    win.delete ('1.0', tk.END)
    win.insert (tk.END, legs_shoulders_2)

def program_3_3 (): # выводим тренировку: ноги + плечи в окно - 3 неделя
    win.delete ('1.0', tk.END)
    win.insert (tk.END, legs_shoulders_3)

# ---------------------- 1. Создаем основное окно -----------------------

root = Tk ()
root.title ('Система тренировок')
root.geometry ('750x706+50+50')
root.config (bg = 'DarkGrey')

# ---------------------- 3. Создаем кнопки и лейблы -----------------------

tk.Button (root, text="Готовая тренировка", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="black",
           command=programs).grid(row=1, column=0, sticky="we", padx=7, pady=7)

tk.Button (root, text="Выбрать схему упражнений", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="black").\
    grid(row=2, column=0, sticky="we", padx=7, pady=7)

tk.Button (root, text="Обратная связь", bg="LightGrey", font=("Comic Sans MS", 12, "normal"), fg="black").\
    grid(row=3, column=0, sticky="we", padx=7, pady=7)

tk.Label (root, text=" ", bg = "DarkGrey").grid(row=4, column=0)
tk.Label (root, text=" ", bg = "DarkGrey").grid(row=5, column=0)
tk.Label (root, text=" ", bg = "DarkGrey").grid(row=6, column=0)
tk.Label (root, text=" ", bg = "DarkGrey").grid(row=7, column=0)
tk.Label (root, text=" ", bg = "DarkGrey").grid(row=8, column=0)
tk.Label (root, text=" ", bg = "DarkGrey").grid(row=9, column=0)
tk.Label (root, text=" ", bg = "DarkGrey").grid(row=10, column=0)
tk.Label (root, text=" ", bg = "DarkGrey").grid(row=11, column=0)
tk.Label (root, text=" ", bg = "DarkGrey").grid(row=12, column=0)
tk.Label (root, text=" ", bg = "DarkGrey").grid(row=13, column=0)
tk.Label (root, text=" ", bg = "DarkGrey").grid(row=14, column=0)
tk.Label (root, text=" ", bg = "DarkGrey").grid(row=15, column=0)
tk.Label (root, text=" ", bg = "DarkGrey").grid(row=16, column=0)
tk.Label (root, text=" ", bg = "DarkGrey").grid(row=17, column=0)
tk.Label (root, text=" ", bg = "DarkGrey").grid(row=18, column=0)
tk.Label (root, text=" ", bg = "DarkGrey").grid(row=19, column=0)

# ---------------------- 4. Создаем окно для вывода информации -----------------------

win = tk.Text(root, width=30, height=30, bg="white", font=("Arial", 14, "normal"))
win.grid(row=1, column=4, rowspan=19)

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
root.grid_rowconfigure(6, minsize=20)
root.grid_rowconfigure(7, minsize=20)
root.grid_rowconfigure(8, minsize=20)
root.grid_rowconfigure(9, minsize=20)
root.grid_rowconfigure(10, minsize=20)
root.grid_rowconfigure(11, minsize=20)
root.grid_rowconfigure(12, minsize=20)
root.grid_rowconfigure(13, minsize=20)
root.grid_rowconfigure(14, minsize=20)
root.grid_rowconfigure(15, minsize=20)
root.grid_rowconfigure(16, minsize=20)
root.grid_rowconfigure(17, minsize=20)
root.grid_rowconfigure(18, minsize=20)

# ---------------------- 2. Закрываем программу -----------------------

root.mainloop ()

# --------------- TO-DO -----------------

# написать визуал программы с выводом информации на экран
# сделать так, чтобы при выборе системы тренировок, к примеру, ноги + плечи, варианты тренировок пропадали (1,2,
# 3) у остальных тренировок, а также разблокировались кнопки систем тренировок
# возможность выбрать по отдельности часть тела для выдачи в результате упражнений