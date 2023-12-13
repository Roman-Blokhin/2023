from tkinter import *

# ----------------------------- ОКНО -----------------------------

# 1. создали основу для программы, окно
root = Tk()
root.title('Блокнот')
root.geometry('650x450+200+200')
root.iconbitmap(default='logo.ico')

# ----------------------------- МЕНЮ -----------------------------

main_menu = Menu(root)  # 4. создаем главное меню

# 6.1 меню - Файл
file_menu = Menu(main_menu, tearoff=0)  # tearoff=0 - убирает ненужную пунктирную линию из меню
file_menu.add_command(label='Открыть')  # добавляем слоты для команд
file_menu.add_command(label='Сохранить')
file_menu.add_separator()  # добавили полоску разделитель
file_menu.add_command(label='Выход')
root.config(menu=file_menu)  # устанавливаем меню в наше окно

# 8.1 меню - Настройки
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Темная')
view_menu_sub.add_command(label='Светлая')
view_menu.add_cascade(menu=view_menu_sub, label='Тема')

# font_menu = Menu(settings_menu, tearoff=0)
root.config(menu=view_menu)

# 9.1 меню - Информация
info_menu = Menu(main_menu, tearoff=0)
info_menu.add_command(label='О нас')
root.config(menu=info_menu)

main_menu.add_cascade(label='Файл', menu=file_menu)  # 7. выводим каскад меню на экран
main_menu.add_cascade(label='Настройки', menu=view_menu)  # 8. выводим каскад меню на экран
main_menu.add_cascade(label='Информация', menu=info_menu)  # 9. выводим каскад меню на экран

root.config(menu=main_menu)  # 5. устанавливаем меню в наше окно(всегда в конце)
# ----------------------------- ФРЕЙМ(КОНТЕЙНЕР) -----------------------------

f_text = Frame(root)  # 2. создали контейнер для текстового поля
f_text.pack(fill=BOTH,  # растягивание по сторонам х и у
            expand=1)  # виджет заполняющий все пространство экрана

# ----------------------------- ТЕКСТОВОЕ ПОЛЕ -----------------------------

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

# ----------------------------- пАНЕЛЬ ПРОКРУТКИ -----------------------------

# 4. добавляем панель прокрутки текста вниз по оси Y
scroll = Scrollbar(f_text, command=text_fild.yview)  # встроенный виджет для прокрутки по вертикали
scroll.pack(fill=Y, side=LEFT)
text_fild.config(yscrollcommand=scroll.set)

# ----------------------------- ВАЖНОЕ -----------------------------

root.mainloop()
