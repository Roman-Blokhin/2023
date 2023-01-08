from tkinter import *

root = Tk ()
root.title ('Game. Remember the word')
root.geometry ('350x350+200+200')
root.config (bg = 'pink')

Label (text = 'Запомни слово', bg = 'pink').grid (row=0, column=0, columnspan=5)
Button (text = 'Начать').grid (row=1, column=0)

entry_1 = Entry (root, justify = RIGHT)
entry_1.grid (row = 2, column = 0)

Label (text = 'Введите слово: ').grid (row=3, column=0)

entry_2 = Entry (root, justify = RIGHT)
entry_2.grid (row = 4, column = 0)

Button (text = 'Сравнить').grid (row=5, column=0)

root.grid_columnconfigure(0, minsize = 50)
root.grid_columnconfigure(1, minsize = 50)
root.grid_columnconfigure(2, minsize = 50)
root.grid_columnconfigure(3, minsize = 50)
root.grid_columnconfigure(4, minsize = 50)
root.grid_columnconfigure(5, minsize = 50)
root.grid_columnconfigure(6, minsize = 50)

root.mainloop ()