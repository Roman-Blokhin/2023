# Pygame. Клеточное поле, Поле в клетку

import pygame
pygame.init()

size = (510, 510)
width = height = 40
count_blocks = 10
margin = 10

FRAME_COLOR = (0, 0, 0)
red = (150, 0, 0)
green = (0, 150, 0)
white = (255, 255, 255)

win = pygame.display.set_mode(size)
pygame.display.set_caption('Клеточное поле')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Выход')
            quit()
    win.fill(red)

    for row in range(count_blocks):
        for column in range(count_blocks):
            x = column*width + (column+1)*margin # меняем координату Х - колонку умножаем на ширину блока и суммируем с
            # отступом умноженным на (колонку + 1) - так мы чередуем номер наших колонок
            y = row*width + (row+1)*margin
            pygame.draw.rect(win, white, (x, y, width, height))

    pygame.display.update()
