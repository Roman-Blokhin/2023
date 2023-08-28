# Pygame. Клеточное поле, Поле в клетку

import pygame
pygame.init()

size = (510, 510)
width = height = 40
count_blocks = 10
margin = 10

black = (0, 0, 0)
red = (150, 0, 0)
green = (0, 150, 0)
white = (255, 255, 255)

win = pygame.display.set_mode(size)
pygame.display.set_caption('Клеточное поле')

# создаем список из 10 нулей, чтобы использовать его для наших блоков
mas = [[0]*10 for i in range(10)]

while True:
    win.fill(red)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Выход')
            quit()

        # условие, где при нажатии кнопки мыши будут сохраняться координаты
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos() # координаты нажатия мыши
            print('x = ' + str(x_mouse) + ' y = ' + str(y_mouse))
            # зная координаты нажатия мышки, мы сможем понять, к какой колонке оно относится
            column = x_mouse // (width+margin) # определяем колонку при нажатии
            row = y_mouse // (height+margin) # определяем ряд при нажатии
            mas [row] [column] = 1 # нажатой колонке и ряду присваиваем значение 1

    for row in range(count_blocks):
        for column in range(count_blocks):
            if mas [row] [column] == 1:
                color = white
            else:
                color = black
            x = column*width + (column+1)*margin # меняем координату Х - колонку умножаем на ширину блока и суммируем с
            # отступом умноженным на (колонку + 1) - так мы чередуем номер наших колонок
            y = row*height + (row+1)*margin
            pygame.draw.rect(win, color, (x, y, width, height))

    pygame.display.update()
