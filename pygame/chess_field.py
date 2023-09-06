import pygame
pygame.init()

brown = (165, 42, 42)
red = (255, 0, 0)

block_size = 50
block_count = 8
margin = 1
width = height = block_size*block_count + margin*9
size = (width, height)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Шахматы')

mas = [[0]*block_count for i in range(block_count)]

run = True

while run:
    screen.fill(brown)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    for row in range(block_size):
        for column in range(block_size):
            #if mas [row][column] == '1':
            #    color = red
#
            #else:
            #    color = red

            pygame.draw.rect(screen, red, (0, 0, block_size, block_size))

    pygame.display.update()