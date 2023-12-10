from tkinter import *
import random as r


def com_1():
    num_1 = r.randint(0, 10)
    num_2 = r.randint(0, 10)

    win.delete(0, END)
    win.insert(END, num_1)
    win_2.delete(0, END)
    win_2.insert(END, num_2)

    if num_1 > num_2:
        Label(root, text='', font=("Comic Sans MS", 12, "normal"), bg='pink').grid(row=6, column=0)
        Label(root, text=' ПОБЕДИЛ 1 ИГРОК', font=("Comic Sans MS", 12, "normal"), bg='pink').grid(row=7, column=0)
    elif num_1 == num_2:
        Label(root, text='', font=("Comic Sans MS", 12, "normal"), bg='pink').grid(row=6, column=0)
        Label(root, text='НИЧЬЯ                    ', font=("Comic Sans MS", 12, "normal"), bg='pink').\
            grid(row=7, column=0)
    else:
        Label(root, text='', font=("Comic Sans MS", 12, "normal"), bg='pink').grid(row=6, column=0)
        Label(root, text=' ПОБЕДИЛ 2 ИГРОК', font=("Comic Sans MS", 12, "normal"), bg='pink').grid(row=7, column=0)


root = Tk()
root.geometry('300x300+150+150')
root.config(bg='pink')

btn1 = Button(root, text='Старт', font=("Comic Sans MS", 12, "normal"), command=com_1)
btn1.grid(row=1, column=0)

Label(root, text='', bg='pink', font=("Comic Sans MS", 12, "normal")).grid(row=0, column=0)
Label(root, text='', bg='pink', font=("Comic Sans MS", 12, "normal")).grid(row=0, column=2)
Label(root, text='', bg='pink', font=("Comic Sans MS", 12, "normal")).grid(row=2, column=2)
Label(root, text='ПЕРВЫЙ ИГРОК: ', bg='pink', font=("Comic Sans MS", 12, "normal")).grid(row=3, column=0)
Label(root, text='', bg='pink', font=("Comic Sans MS", 12, "normal")).grid(row=4, column=0)
Label(root, text='ВТОРОЙ ИГРОК: ', bg='pink', font=("Comic Sans MS", 12, "normal")).grid(row=5, column=0)

win = Entry(root, width=3, font=("Comic Sans MS", 12, "normal"))
win.grid(row=3, column=1)

win_2 = Entry(root, width=3, font=("Comic Sans MS", 12, "normal"))
win_2.grid(row=5, column=1)

root.grid_rowconfigure(0, minsize=30)
root.grid_rowconfigure(1, minsize=30)
root.grid_rowconfigure(2, minsize=30)
root.grid_columnconfigure(0, minsize=100)
root.grid_columnconfigure(1, minsize=100)
root.grid_columnconfigure(2, minsize=100)

root.mainloop()
