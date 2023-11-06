from tkinter import *


def exit():
    root.destroy()


def python_btn():
    b0 = Button(root, text='PYTHON', command=python_btn)
    b0.grid(row=1, column=1, columnspan=3, sticky='we')

    b1 = Button(root, text='1')
    b1.grid(row=2, column=1, sticky='swen', padx=0, pady=5)
    b2 = Button(root, text='2')
    b2.grid(row=2, column=2, sticky='swen', padx=0, pady=5)
    b3 = Button(root, text='3')
    b3.grid(row=2, column=3, sticky='swen', padx=0, pady=5)

    b4 = Button(root, text='4')
    b4.grid(row=3, column=1, sticky='swen', padx=0, pady=5)
    b5 = Button(root, text='5')
    b5.grid(row=3, column=2, sticky='swen', padx=0, pady=5)
    b6 = Button(root, text='6')
    b6.grid(row=3, column=3, sticky='swen', padx=0, pady=5)

    b7 = Button(root, text='7')
    b7.grid(row=4, column=1, sticky='swen', padx=0, pady=5)
    b8 = Button(root, text='8')
    b8.grid(row=4, column=2, sticky='swen', padx=0, pady=5)
    b9 = Button(root, text='9')
    b9.grid(row=4, column=3, sticky='swen', padx=0, pady=5)


def html_btn():
    b0 = Button(root, text='HTML', command=python_btn)
    b0.grid(row=1, column=1, columnspan=3, sticky='we')

    b1 = Button(root, text='1')
    b1.grid(row=2, column=1, sticky='swen', padx=0, pady=5)
    b2 = Button(root, text='2')
    b2.grid(row=2, column=2, sticky='swen', padx=0, pady=5)
    b3 = Button(root, text='3')
    b3.grid(row=2, column=3, sticky='swen', padx=0, pady=5)

    b4 = Button(root, text='4')
    b4.grid(row=3, column=1, sticky='swen', padx=0, pady=5)
    b5 = Button(root, text='5')
    b5.grid(row=3, column=2, sticky='swen', padx=0, pady=5)
    b6 = Button(root, text='6')
    b6.grid(row=3, column=3, sticky='swen', padx=0, pady=5)

    b7 = Button(root, text='7')
    b7.grid(row=4, column=1, sticky='swen', padx=0, pady=5)
    b8 = Button(root, text='8')
    b8.grid(row=4, column=2, sticky='swen', padx=0, pady=5)
    b9 = Button(root, text='9')
    b9.grid(row=4, column=3, sticky='swen', padx=0, pady=5)


def sql_btn():
    b0 = Button(root, text='SQL', command=python_btn)
    b0.grid(row=1, column=1, columnspan=3, sticky='we')

    b1 = Button(root, text='1')
    b1.grid(row=2, column=1, sticky='swen', padx=0, pady=5)
    b2 = Button(root, text='2')
    b2.grid(row=2, column=2, sticky='swen', padx=0, pady=5)
    b3 = Button(root, text='3')
    b3.grid(row=2, column=3, sticky='swen', padx=0, pady=5)

    b4 = Button(root, text='4')
    b4.grid(row=3, column=1, sticky='swen', padx=0, pady=5)
    b5 = Button(root, text='5')
    b5.grid(row=3, column=2, sticky='swen', padx=0, pady=5)
    b6 = Button(root, text='6')
    b6.grid(row=3, column=3, sticky='swen', padx=0, pady=5)

    b7 = Button(root, text='7')
    b7.grid(row=4, column=1, sticky='swen', padx=0, pady=5)
    b8 = Button(root, text='8')
    b8.grid(row=4, column=2, sticky='swen', padx=0, pady=5)
    b9 = Button(root, text='9')
    b9.grid(row=4, column=3, sticky='swen', padx=0, pady=5)


root = Tk()
root.title('')
root.geometry('950x650+100+100')
root.config(bg='')

# --------------------------- #

lbl1 = Label(root, text='')
lbl1.grid(row=0, column=0)

lbl1 = Label(root, text='')
lbl1.grid(row=0, column=4)

lbl1 = Label(root, text='')
lbl1.grid(row=0, column=5)

# --------------------------- #

btn1 = Button(root, text='PYTHON', command=python_btn)
btn1.grid(row=1, column=1, columnspan=3, sticky='we')

btn1 = Button(root, text='HTML', command=html_btn)
btn1.grid(row=2, column=1, columnspan=3, sticky='we')

btn1 = Button(root, text='SQL', command=sql_btn)
btn1.grid(row=3, column=1, columnspan=3, sticky='we')

# --------------------------- #

win = Text(root, bg='grey')
win.grid(row=1, column=6, rowspan=10)

# --------------------------- #

root.grid_columnconfigure(0, minsize=50)
root.grid_columnconfigure(1, minsize=50)
root.grid_columnconfigure(2, minsize=50)
root.grid_columnconfigure(3, minsize=50)
root.grid_columnconfigure(4, minsize=50)

root.grid_rowconfigure(0, minsize=10)
root.grid_rowconfigure(1, minsize=10)
root.grid_rowconfigure(2, minsize=10)
root.grid_rowconfigure(3, minsize=10)

# --------------------------- #

root.mainloop()
