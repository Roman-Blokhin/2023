from tkinter import *

root = Tk()
root.geometry ('180x130+300+300')
root.config(bg='pink')

btn1 = Button(root, text='привет')
btn1.grid(row=1, column=1)
btn2 = Button(root, text='пока')
btn2.grid(row=1, column=3)

Label(root, text='', bg='pink').grid(row=0, column=0)
Label(root, text='', bg='pink').grid(row=0, column=2)

root.grid_rowconfigure(0, minsize=30)
root.grid_columnconfigure(0, minsize=30)
root.grid_columnconfigure(2, minsize=30)

root.mainloop()