from tkinter import *

root = Tk ()
root.title ('Bones')
root.geometry ('350x350+200+200')
root.config (bg = 'lightgreen')

label_0 = Label (root, text='Вам нужно кинуть кубики, чтобы понять, у кого результат больше', bg = 'lightgreen')
label_0.grid(row=0, column=0, columnspan=3, sticky='wens')

frame_1 = LabelFrame (root, text='Игрок', bg = 'lightgreen')
frame_1.grid (row=1, column=0, sticky='wens')

label_1 = Label(frame_1, width=7, height=4, bg='yellow', text="1")
label_1.grid(row=1, column=1, sticky='wens')

frame_2 = LabelFrame (root, text='Компьютер', bg = 'lightgreen')
frame_2.grid (row=1, column=1, sticky='wens')

label_2 = Label(frame_2, width=7, height=4, bg='yellow', text="2")
label_2.grid(row=1, column=2, sticky='wens')

root.mainloop ()