import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

def main():
    pygame.init()
    screen_width = 800
    screen_height = 600
    display = pygame.display.set_mode((screen_width, screen_height))
    bg_color = 	(0, 0, 0)
    pygame.display.set_caption("Star")
    display_rect = display.get_rect()
    stars = Group()
    create_fleet(display, screen_width, screen_height,stars)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        stars.draw(display)
        pygame.display.flip()

class Alien(Sprite):
    def __init__(self, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

def get_number_aliens_x(screen_width, alien_width):
    available_space_x = screen_width - alien_width
    number_aliens_x = int(available_space_x / (alien_width))
    return number_aliens_x

def get_number_rows(screen_height, alien_height):
    available_space_y = (screen_height - (2 * alien_height))
    number_rows = int(available_space_y / (alien_height))
    return number_rows

def create_alien(screen, aliens, alien_number, row_number):
    alien = Alien(screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(screen, screen_width, screen_height,aliens):
    alien = Alien(screen)
    number_aliens_x = get_number_aliens_x(screen_width, alien.rect.width)
    number_rows = get_number_rows(screen_height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(screen, aliens, alien_number, row_number)

main()
        