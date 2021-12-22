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
size = width, height = (300, 300)


class Creature(pygame.sprite.Sprite):
    image = load_image("creature.png")

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Creature.image
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20

    def update(self, *args):
        if args and args[0].type == pygame.KEYUP:
            if args[0].key == pygame.K_UP:
                self.rect.y -= 10
            elif args[0].key == pygame.K_DOWN:
                self.rect.y += 10
            elif args[0].key == pygame.K_LEFT:
                self.rect.x -= 10
            elif args[0].key == pygame.K_RIGHT:
                self.rect.x += 10


screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
c = Creature(all_sprites)
running = True
cords_mouse = None, None
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            all_sprites.update(event)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
pygame.quit()