import pygame
pygame.init()

block_size = 100
margin = 15
block_count = 3
width = block_size*block_count + margin*4
height = block_size*block_count + margin*4
size = (width, height)

grey = (50, 50, 50)
white = (255, 255, 255)
red = (105, 0, 0)
green = (0, 150, 0)
blue = (0, 0, 150)
PapayaWhip = (255, 239, 213)

mas = [[0]*block_count for i in range(block_count)]

query = 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Крестики нолики')

run = True
while run:
    screen.fill(PapayaWhip)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Выход')
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            column = x_mouse // (block_size+margin)
            row = y_mouse // (block_size+margin)
            if mas [row] [column] == 0:
                if query % 2 == 0:
                    mas [row] [column] = 'x'
                    print('Ходит игрок: Х')
                    print('x = ' + str(x_mouse) + ' y = ' + str(y_mouse))
                else:
                    mas [row] [column] = 'o'
                    print('Ходит игрок: О')
                    print('x = ' + str(x_mouse) + ' y = ' + str(y_mouse))
            query += 1

    for row in range(block_count):
        for column in range(block_count):
            if mas [row] [column] == 'x':
                color = green

            elif mas [row] [column] == 'o':
                color = blue

            else:
                color = grey
            x = column*block_size + (column+1)*margin
            y = row*block_size + (row+1)*margin
            pygame.draw.rect(screen, color, (x, y, block_size, block_size))
            if color == green:
                pygame.draw.line(screen, white, (x+20, y+20), (x + block_size-20, y + block_size-20), 3)
                pygame.draw.line(screen, white, (x+block_size-20, y+20), (x+20, y + block_size-20), 3)
            elif color == blue:
                pygame.draw.circle(screen, white, (x+block_size/2, y+block_size/2), 35, 3)

    pygame.display.update()

