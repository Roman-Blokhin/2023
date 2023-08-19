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

width_q = 20 # ширина объекта
height_q = 20 # высота объекта

x = WIDTH/2 # координаты расположение на оси х
y = HEIGHT/2 # координаты расположение на оси y

velocity = 1 # скорость

# определяем класс для создания персонажа
class Player (pygame.sprite.Sprite):
    def __init__(self): # запускает наш код при создании персонажа
        pygame.sprite.Sprite.__init__(self) # запускаем инициализатор встроенных классов Sprite
        self.image = pygame.Surface((350, 350)) # задаем размер нашего персонажа - квадрат
        self.image.fill(BLACK) # задаем цвет квадрата
        self.rect = self.image.get_rect() # создаем прямоугольник, окружающий наш квадрат для
        #self.rect.center = (WIDTH/2, HEIGHT/2) # размещаем прямоугольник по центру экрана
        #pygame.display.update() # ОБЪЕКТ ВЫВОДИТСЯ НА ЭКРАН


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(SKY)
pygame.display.set_caption('WarCraft')
pygame.display.flip()
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group() # создали группу для спрайтов (элементов, которые двигаются на экране)
player = Player() # создали спрайт персонажа
all_sprites.add(player) # добавили спрайт персонажа в группу спрайтов


running = True
while running:
    pygame.time.delay(10) # время передвижения в миллисекундах

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= velocity
    elif keys[pygame.K_RIGHT] and x < 300:
        x += velocity
    if keys[pygame.K_UP] and y > 0:
        y -= velocity
    elif keys[pygame.K_DOWN] and x < 400:
        y += velocity

    pygame.draw.rect(screen, WHITE, (x, y, width_q, height_q)) # НАРИСОВАЛИ ОБЪЕКТ И РАЗМЕСТИЛИ ЕГО
    pygame.display.update()
    #all_sprites.update() # добавили группу спрайтов в цикл

pygame.quit()