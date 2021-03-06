import pygame
import random

NEGRO = (0, 0, 0)


class Moneda(pygame.sprite.Sprite):

    def __init__(self, image, limites):
        super().__init__()
        self.image = pygame.image.load(image[random.randint(0, 2)])
        self.rect = self.image.get_rect()
        self.limite_izquierdo = 8
        self.limite_derecho = limites[0] - 8
        self.limite_superior = 8
        self.limite_inferior = limites[1] - 8
        self.cambio_x = 0
        self.cambio_y = 0

    def update(self):
        self.rect.x += self.cambio_x
        self.rect.y += self.cambio_y
        if self.rect.right >= self.limite_derecho or self.rect.left <= self.limite_izquierdo:
            self.cambio_x *= -1
        if self.rect.bottom >= self.limite_inferior or self.rect.top <= self.limite_superior:
            self.cambio_y *= -1
