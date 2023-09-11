import pygame
pygame.init()

brown = (139, 69, 19)
litebrown = (188, 143, 143)
red = (255, 0, 0)
white = (255, 228, 196)
green = (32, 178, 170)
grey = (112, 128, 144)

block_size = 50
block_count = 8
margin = 1
header_margin = block_size
width = height = block_size*block_count + 2*block_size + margin*block_count
size = (width, height)

def blocks(color, row, column):
    pygame.draw.rect(screen, color, [block_size+column*block_size + margin*(column + 1),
                                     block_size+row*block_size + margin*(row + 1),
                                     block_size, block_size])

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Шахматы')

mas = [[0]*block_count for i in range(block_count)]

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            column = x_mouse // (block_size+margin)
            row = y_mouse // (block_size+margin)
            print('x =', x_mouse, 'y =', y_mouse, 'column =', column, 'row =', row)

    screen.fill(grey)

    for row in range(block_count):
        for column in range(block_count):
            x = column*block_size + (column+1)*margin + header_margin*2
            y = row*block_size + (row+1)*margin

            if (row+column) % 2 == 0:
                color = white
            else:
                color = green

            blocks(color, row, column)

            if color == green:
                pygame.draw.line(screen, white, (x+10, y+10), (x+block_size-20, y+block_size-20), 3)



    pygame.display.update()