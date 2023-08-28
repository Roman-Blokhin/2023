import pygame
pygame.init()

block_size = 100
margin = 15
block_count = 3
width = block_size*block_count + margin*4
height = block_size*block_count + margin*4
size = (width, height)

grey = (100, 100, 100)
white = (255, 255, 255)
red = (105, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

mas = [[0]*block_count for i in range(block_count)]

screen = pygame.display.set_mode(size)

run = True
while run:
    screen.fill(red)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Выход')
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print('x = ' + str(x_mouse) + ' y = ' + str(y_mouse))
            column = x_mouse // (block_size+margin)
            row = y_mouse // (block_size+margin)
            mas [row] [column] = mas [row] [column] ^ 1

    for row in range(block_count):
        for column in range(block_count):
            if mas [row] [column] == 1:
                color = white
            else:
                color = grey
            x = column*block_size + (column+1)*margin
            y = row*block_size + (row+1)*margin
            pygame.draw.rect(screen, color, (x, y, block_size, block_size))

    pygame.display.update()