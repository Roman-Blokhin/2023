from tkinter import *
import random as r


def com_1():
    num_1 = r.randint(0, 100)
    num_2 = r.randint(0, 100)

    win.delete(0, END)
    win.insert(END, num_1)
    win_2.delete(0, END)
    win_2.insert(END, num_2)


root = Tk()
root.geometry('200x130+300+300')
root.config(bg='pink')

btn1 = Button(root, text='Старт', command=com_1)
btn1.grid(row=1, column=1, columnspan=3)

Label(root, text='', bg='pink').grid(row=0, column=0)
Label(root, text='', bg='pink').grid(row=0, column=2)
Label(root, text='', bg='pink').grid(row=2, column=2)

win = Entry(root, width=3)
win.grid(row=3, column=1)

win_2 = Entry(root, width=3)
win_2.grid(row=3, column=3)

root.grid_rowconfigure(0, minsize=30)
root.grid_columnconfigure(0, minsize=30)
root.grid_columnconfigure(2, minsize=30)

root.mainloop()
