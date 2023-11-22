import pygame

class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('SidewayShip.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.x = self.screen_rect.left

        self.moving_up = False
        self.moving_down = False

    def updates(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1

        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    