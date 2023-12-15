from tkinter import *
import random as r


# функция выбора варианта компьютером из списка значений и вывод результата
def starting():
    ssp = ('Камень', 'Ножницы', 'Бумага')
    value = r.choice(ssp)  # рандомный выбор из списка
    comp_var.config(text=value)  # меняем параметр text у comp_var


root = Tk()
root.title('Камень ножницы бумага')
root.geometry('450x350+200+200')
root.config(bg='black')
root.resizable(width=False, height=False)

# кнопки для выбора варианта пользователем
stone = Button(root, text='Камень', font=('Comic Sans MS', 14), command=starting)
stone.place(x=40, y=200)

scissors = Button(root, text='Ножницы', font=('Comic Sans MS', 14), command=starting)
scissors.place(x=170, y=200)

paper = Button(root, text='Бумага', font=('Comic Sans MS', 14), command=starting)
paper.place(x=330, y=200)

# рандомный вариант компьютера
comp_var = Label(root, text='', font=('Comic Sans MS', 14), fg='white', bg='black')
comp_var.place(x=180, y=100)

root.mainloop()
