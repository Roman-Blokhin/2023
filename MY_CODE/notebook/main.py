from tkinter import *

# 1. создали основу для программы, окно

root = Tk()
root.title('Блокнот')
root.geometry('650x450+200+200')
root.iconbitmap(default='logo.ico')

f_text = Frame(root)  # 2. создали контейнер для текстового поля
f_text.pack(fill=BOTH,  # растягивание по сторонам х и у
            expand=1)  # виджет заполняющий все пространство экрана

text_fild = Text(f_text,
                 bg='black',
                 fg='lime',
                 padx=10,
                 pady=10,
                 wrap=WORD,  # ПЕРЕНОС ТЕКСТА ПО СЛОВАМ
                 insertbackground='brown',  # ДОБАВЛЯЕМ КУРСОР, УКАЗЫВАЕМ ЦВЕТ
                 selectbackground='#8D917A',  # ЦВЕТ ВЫДЕЛЕННОГО ТЕКСТА
                 spacing3=10,  # ДОБАВИЛИ ОТСТУПЫ У АБЗАЦЕВ
                 width=30  # ШИРИНА СКРОЛЛБАРА
                 )
text_fild.pack(fill=BOTH, expand=1, side=LEFT)  # 3. side=LEFT - выравнивание по левой стороне контейнера

# 4. добавляем панель прокрутки текста вниз по оси Y
scroll = Scrollbar(f_text, command=text_fild.yview)  # встроенный виджет для прокрутки по вертикали
scroll.pack(fill=Y, side=LEFT)
text_fild.config(yscrollcommand=scroll.set)

root.mainloop()
