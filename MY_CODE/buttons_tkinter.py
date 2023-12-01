from tkinter import *
import random as r


def com_1():
    num_1 = r.randint(0, 100)
    Label(root, text=num_1).grid(row=2, column=1)


def com_2():
    num_2 = r.randint(0, 100)
    Label(root, text=num_2).grid(row=2, column=3)


root = Tk()
root.geometry('200x130+300+300')
root.config(bg='pink')

btn1 = Button(root, text='Игрок 1', command=com_1)
btn1.grid(row=1, column=1)
btn2 = Button(root, text='Игрок 2', command=com_2)
btn2.grid(row=1, column=3)

Label(root, text='', bg='pink').grid(row=0, column=0)
Label(root, text='', bg='pink').grid(row=0, column=2)
Label(root, text='', bg='pink').grid(row=2, column=2)

win = Entry(root)
win.grid(row=3, column=1, columnspan=5)

root.grid_rowconfigure(0, minsize=30)
root.grid_columnconfigure(0, minsize=30)
root.grid_columnconfigure(2, minsize=30)

root.mainloop()
