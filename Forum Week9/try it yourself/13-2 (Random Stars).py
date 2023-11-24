import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import randint

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

class Stars(Sprite):
    def __init__(self, screen):
        super(Stars, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('IMAGES/star.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

def get_number_stars_x(screen_width, star_width):
    available_space_x = screen_width - star_width
    num_stars_x = int(available_space_x / (star_width))
    return num_stars_x

def get_number_rows(screen_height, star_height):
    available_space_y = (screen_height - (2 * star_height))
    number_rows = int(available_space_y / (star_height))
    return number_rows

def create_star(screen, stars, star_number, row_number):
    random_number = randint(-10, 10)
    random_number1 = randint(-10, 10)
    star = Stars(screen)
    star_width = star.rect.width
    star.x = star_width + random_number * star_width * star_number
    star.rect.x = star.x
    star.rect.y = star.rect.height + random_number1 * star.rect.height * row_number
    stars.add(star)

def create_fleet(screen, screen_width, screen_height, stars):
    star = Stars(screen)
    number_stars_x = get_number_stars_x(screen_width, star.rect.width)
    number_rows = get_number_rows(screen_height, star.rect.height)

    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(screen, stars, star_number, row_number)

main()