# Pygame. Клеточное поле, Поле в клетку

import pygame
pygame.init()

size = (500,500)

FRAME_COLOR = (0, 0, 0)
RED = (150, 0, 0)
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)

win = pygame.display.set_mode(size)
pygame.display.set_caption('Клеточное поле')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Выход')
            quit()
    win.fill(FRAME_COLOR)

    pygame.display.update()
