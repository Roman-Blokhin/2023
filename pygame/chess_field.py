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

    screen.fill(grey)

    for row in range(block_count):
        for column in range(block_count):
            if (row+column) % 2 == 0:
                color = white
            else:
                color = green

            blocks(color, row, column)

    pygame.display.update()