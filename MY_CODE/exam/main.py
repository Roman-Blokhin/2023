from tkinter import *

root = Tk()
root.title('')
root.geometry('350x350+200+200')
root.config(bg='')

# --------------------------- #

lbl1 = Label(root, text='fdgdfg', bg='grey')
lbl1.grid(row=0, column=1)

lbl1 = Label(root, text='fdgdfg', bg='grey')
lbl1.grid(row=0, column=0)

lbl1 = Label(root, text='fdgdfg', bg='grey')
lbl1.grid(row=0, column=2)

# --------------------------- #

btn1 = Button(root, text='fdgdfg')
btn1.grid(row=1, column=1)

btn1 = Button(root, text='fdgdfg')
btn1.grid(row=2, column=1)

btn1 = Button(root, text='fdgdfg')
btn1.grid(row=3, column=1)

# --------------------------- #

win = Text(root, bg='pink')
win.grid(row=1, column=3)

root.mainloop()
