import pygame

FRAME_COLOR = (0, 0, 0)
BLUE = (135, 206, 235)
WHITE = (255, 255, 255)

SIZE = [400, 400]
SIZE_BLOCK = 20
MARGIN = 1

COUNT_BLOCKS = 20


screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Snake')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)

    # создаем вложенный цикл, к котороый создает столбцы и колонки определенных цветов с отступами
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, [0 + column * SIZE_BLOCK + MARGIN * (column + 1),
                                             0 + row * SIZE_BLOCK + MARGIN * (row + 1),
                                             SIZE_BLOCK,
                                             SIZE_BLOCK])

    pygame.display.flip()

