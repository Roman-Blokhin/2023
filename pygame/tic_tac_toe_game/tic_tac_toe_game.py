import pygame
pygame.init()

block_size = 100 # размер клеток
margin = 15 # размер отступов между клетками
width = height = block_size*3 + margin*4 # ширина и длина окна
size_window = (width, height)

FRAME_COLOR = (0, 0, 0)
RED = (150, 0, 0)
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)

mas = [[0]*3 for i in range (3)] # массив с нулями. нули означают, что клетка пустая

win = pygame.display.set_mode(size_window)
pygame.display.set_caption('Крестики-Нолики')
img = pygame.image.load('tic_tac_icon.png')
pygame.display.set_icon(img)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Выход')
            quit()
    win.fill(FRAME_COLOR)

    pygame.display.update()
