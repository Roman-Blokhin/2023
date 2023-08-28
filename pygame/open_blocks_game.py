import pygame
pygame.init()

block_size = 100
margin = 15
block_count = 3
width = block_size*block_count + margin*4
height = block_size*block_count + margin*4
size = (width, height)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode(size)

run = True
while run:
    screen.fill(red)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Выход')
            quit()

    for row in range(block_count):
        for column in range(block_count):
            x = column*block_size + (column+1)*margin
            y = row*block_size + (row+1)*margin
            pygame.draw.rect(screen, black, (x, y, block_size, block_size))

    pygame.display.update()