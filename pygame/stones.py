import random as ra
import pygame

black = (0, 0, 0)
white = (255, 255, 255)
red = (150, 0, 0)
green = (0, 150, 0)
blue = (0, 0, 150)

block_size = 100
margin = 50
header_margin = 150
block_count = 2
width = block_size*2 + margin*2
height = header_margin + block_size
size = (width, height)

firstNumber = ra.randint(1, 6)
secondNumber = ra.randint(1, 6)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('stones..')

run = True
while run:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    for row in range(1):
        for column in range(2):
            x = column*block_size + (column+1) * margin/3
            y = row*block_size + (row+1) * margin
            pygame.draw.rect(screen, black, (x, y, block_size, block_size))
            if column % 2 == 0:
                pygame.draw.rect(screen, black, (x, y, block_size, block_size))

    pygame.display.update()

print('Первый кубик: ', str (firstNumber))
print('Второй кубик: ', str (secondNumber))