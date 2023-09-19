from tkinter import *
import random as r


def rando ():
    a = r.randint(1, 6)
    b = r.randint(1, 6)
    l1 = Label(root, text = a)
    l1.grid(row=1, column=0)
    l2 = Label(root, text = b)
    l2.grid(row=1, column=1)

    if a > b:
        l3 = Label(root, text = 'Игрок 1 победил')
        l3.grid(row=2, column=0, columnspan=2)
    else:
        l4 = Label(root, text = 'Игрок 2 победил')
        l4.grid(row=2, column=0, columnspan=2)


root = Tk()
root.geometry('200x200')

btn1 = Button (root, text = 'Бросить кубики', command=rando)
btn1.grid(row=0, column=0, columnspan=2)






root.mainloop()