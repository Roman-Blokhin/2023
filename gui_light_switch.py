"""I want to do light switch with tkinter"""

from tkinter import *


def off():
    root.config(bg='black')
    one.config(bg='black')
    two.config(bg='black')
    three.config(bg='black')
    btn_1.config(state=DISABLED)
    btn_2.config(state=NORMAL)


def on():
    root.config(bg='white')
    one.config(bg='white')
    two.config(bg='white')
    three.config(bg='white')
    btn_1.config(state=NORMAL)
    btn_2.config(state=DISABLED)


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

btn_1 = Button(bd=5, command=off)
btn_1.grid(row=1, column=1, sticky='wens', padx=5, pady=20)
btn_2 = Button(bd=5, command=on)
btn_2.grid(row=1, column=2, sticky='wens', padx=5, pady=20)

root.grid_columnconfigure(0, minsize=65)
root.grid_columnconfigure(1, minsize=200)
root.grid_columnconfigure(2, minsize=200)

root.grid_rowconfigure(0, minsize=70)
root.grid_rowconfigure(1, minsize=360)

root.mainloop()
