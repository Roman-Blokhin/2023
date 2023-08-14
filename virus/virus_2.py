from tkinter import *
from tkinter import messagebox as mb
import random as r
from random import randint
import webbrowser as wb
import os

def open_git():
    while True:
        wb.open('https://github.com/')
        path = r'C:\\' # добавил открытие папки в цикле
        os.startfile(path)

root = Tk ()
root.title ('')
root.geometry ('350x350+200+200')
root.config (bg = '')

Button (root, text="Не нажимать", command=open_git).pack()

root.mainloop ()