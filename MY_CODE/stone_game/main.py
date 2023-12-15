from tkinter import *


def starting():
    pass


root = Tk ()
root.title ('Камень ножницы бумага')
root.geometry ('450x350+200+200')
root.config (bg = 'black')
root.resizable(width=False, height=False)

values = ['Камень', 'Ножницы', 'Бумага']

stone = Button(root, text='Камень', font=('Comic Sans MS', 14), command=starting)
stone.place(x=40, y=200)

scissors = Button(root, text='Ножницы', font=('Comic Sans MS', 14), command=starting)
scissors.place(x=170, y=200)

paper = Button(root, text='Бумага', font=('Comic Sans MS', 14), command=starting)
paper.place(x=330, y=200)


root.mainloop ()