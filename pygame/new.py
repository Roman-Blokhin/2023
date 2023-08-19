import random
import pygame


WIDTH = 400
HEIGHT = 500
FPS = 30

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
PINK = 255, 0, 255
YELLOW = 255, 255, 0
SKY = 0, 175, 255
WHITE = 255, 255, 255
BLACK = 0, 0, 0


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(SKY)
pygame.display.set_caption('WarCraft')
pygame.display.flip()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() # создали группу для спрайтов (элементов, которые двигаются на экране)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update() # добавили группу спрайтов в цикл


pygame.quit()