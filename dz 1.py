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
size = width, height = (600, 95)


class Creature(pygame.sprite.Sprite):
    image = load_image("car2.png")
    run = 0

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Creature.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.x = 0

    def update(self):
        if Creature.run == 0:
            self.rect.x += 1
            self.x += 1
            if self.x == 449:
                Creature.run = 1
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.rect.x -= 1
            self.x -= 1
            if self.x == 1:
                Creature.run = 0
                self.image = pygame.transform.flip(self.image, True, False)


screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
c = Creature(all_sprites)
running = True
cords_mouse = None, None
fps = 150
clock = pygame.time.Clock()
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()