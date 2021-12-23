import sys
import pygame
import os


def load_image(name, colorkey=-1):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        # image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
size = width, height = (600, 300)


class Bomb(pygame.sprite.Sprite):
    image = load_image("gameover.png")
    image_boom = load_image("gameover.png")

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.rect.y = 0
        self.coord_x = 0

    def update(self):
        if self.coord_x < 600:
            self.rect.x += 1
            self.coord_x += 1

screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
Bomb(all_sprites)
running = True
cords_mouse = None, None
fps = 200
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()