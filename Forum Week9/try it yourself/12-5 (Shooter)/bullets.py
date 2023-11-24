import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, ship):

        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, 10, 5)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right

        self.x = float(self.rect.x)

        self.color = 255,255,255
        self.speed_factor = 1

    def update(self):

        self.x += self.speed_factor

        self.rect.x = self.x

    def draw_bullet(self):

        pygame.draw.rect(self.screen, self.color, self.rect)