import pygame

FRAME_COLOR = (70, 130, 180)
BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
HEADER_COLOR = (173, 216, 230)

COUNT_BLOCKS = 20
SIZE_BLOCK = 20
MARGIN = 1
HEADER_MARGIN = 70

SIZE = [SIZE_BLOCK*COUNT_BLOCKS + 2*SIZE_BLOCK + MARGIN*COUNT_BLOCKS,
        SIZE_BLOCK*COUNT_BLOCKS + 2*SIZE_BLOCK + MARGIN*COUNT_BLOCKS + HEADER_MARGIN]
print(SIZE)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Snake')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, SIZE[0], HEADER_MARGIN])

    # создаем вложенный цикл, который создает столбцы и колонки определенных цветов с отступами
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                             HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                             SIZE_BLOCK,
                                             SIZE_BLOCK])

    pygame.display.flip()

