from tkinter import *
import random as r


def rando():
    a = r.randint(1, 6)
    b = r.randint(1, 6)
    l1 = Label(root, text=a, font=('Arial', 15, 'bold'))
    l1.grid(row=1, column=0, padx=20, pady=20)
    l2 = Label(root, text=b, font=('Arial', 15, 'bold'))
    l2.grid(row=1, column=1, padx=20, pady=20)

    score_1 = 0
    score_2 = 0

    if a > b:
        l3 = Label(root, text='Игрок 1 победил', font=('Arial', 15, 'bold'))
        l3.grid(row=2, column=0, columnspan=2)

        l6 = Label(root, text='Счет:')
        l6.grid(row=3, column=0)
        score_1 += 1

        l7 = Label(root, text=score_1)
        l7.grid(row=4, column=0)

    elif a < b:
        l4 = Label(root, text='Игрок 2 победил', font=('Arial', 15, 'bold'))
        l4.grid(row=2, column=0, columnspan=2)

        l6 = Label(root, text='Счет:')
        l6.grid(row=3, column=0)
        score_2 += 1
        l8 = Label(root, text=score_2)
        l8.grid(row=4, column=1)

    else:
        l5 = Label(root, text='          Ничья          ', font=('Arial', 15, 'bold'))
        l5.grid(row=2, column=0, columnspan=2)


root = Tk()
root.geometry('300x300')

btn1 = Button(root, text='Бросить кубики', font=('Arial', 15, 'bold'), command=rando)
btn1.grid(row=0, column=0, columnspan=2)

root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=150)

root.mainloop()
