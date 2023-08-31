import pygame
pygame.init()

block_size = 100
margin = 15
width = height = block_size*3 + margin*4 # ширина и длина окна
size_window = (width, height)

FRAME_COLOR = (0, 0, 0)
RED = (150, 0, 0)
green = (0, 150, 0)
white = (255, 255, 255)
blue = (0, 0, 155)

query = 0 # переменная для смены игрока

win = pygame.display.set_mode(size_window)
pygame.display.set_caption('Крестики-Нолики')
img = pygame.image.load('tic_tac_icon.png')
pygame.display.set_icon(img)

mas = [[0]*3 for i in range (3)] # массив с нулями. нули означают, что клетка пустая

while True:
    win.fill(FRAME_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Выход')
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print('x = ' + str(x_mouse) + ' y = ' + str(y_mouse))
            col = x_mouse // (block_size+margin)
            row = y_mouse // (block_size+margin)
            if mas [row][col] == 0: # проверка, чтобы нельзя было менять цвет ячейки, если она занята др. игроком
                if query % 2 == 0: # четные, один игрок и цвет, нечетные - другой
                    mas [row][col] = 'x'
                else:
                    mas [row][col] = 'o'
            query += 1

    for row in range (3):
        for col in range (3):
            if mas [row][col] == 'x':
                color = green
            elif mas [row][col] == 'o':
                color = blue
            else:
                color = white
            x = col*block_size + (col+1)*margin
            y = row*block_size + (row+1)*margin
            pygame.draw.rect(win, color, (x, y, block_size, block_size))
            if color == green:
                # чертим линию из одного угла в другой, последний параметр - ширина линии
                pygame.draw.line (win, white, (x+20, y+20), (x+block_size-20, y+block_size-20), 3)
                pygame.draw.line (win, white, (x+block_size-20, y+20), (x+20, y+block_size-20), 3)
            elif color == blue:
                # ищем ширину и высоту квадрата и делим пополам, так находим центр для радиуса
                pygame.draw.circle(win, white, (x+block_size/2, y+block_size/2), 35, 3)

    pygame.display.update()
