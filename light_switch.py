"""I want to do light switch with tkinter"""

from tkinter import *


def off():
    root.config(bg='black')
    one.config(bg='black')
    two.config(bg='black')
    three.config(bg='black')


def on():
    root.config(bg='white')
    one.config(bg='white')
    two.config(bg='white')
    three.config(bg='white')


root = Tk()
root.title('light switch')
root.geometry('525x500+200+200')
root.config(bg='grey')

one = Label(text=' ', bg='grey')
one.grid(row=0, column=0)
two = Label(text=' ', bg='grey')
two.grid(row=1, column=3)
three = Label(text=' ', bg='grey')
three.grid(row=1, column=0)

Button(bd=5, command=off).grid(row=1, column=1, sticky='wens', padx=5, pady=20)
Button(bd=5, command=on).grid(row=1, column=2, sticky='wens', padx=5, pady=20)

root.grid_columnconfigure(0, minsize=65)
root.grid_columnconfigure(1, minsize=200)
root.grid_columnconfigure(2, minsize=200)

root.grid_rowconfigure(0, minsize=70)
root.grid_rowconfigure(1, minsize=360)

root.mainloop()
