import tkinter as tk
from tkinter import *
import random as r

# создал приложение, которое меняет свой размер и координаты при нажатии на кнопку "Закрыть"
def joke ():
    x = str (r.randint (100, 500))
    y = str (r.randint (100, 500))
    xz = str (r.randint (100, 500))
    yz = str (r.randint (100, 500))
    root.geometry (x + 'x' + y + '+' + xz + '+' + yz)
    print (x)
    print (y)
    print (xz)
    print (yz)

root = tk.Tk ()
root.geometry ("400x300+100+100")
root.title ("Безопасное приложение")

Button (root, text="Закрыть", command=joke).pack()

root.mainloop ()