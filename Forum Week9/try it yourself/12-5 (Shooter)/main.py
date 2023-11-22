import sys
import pygame
from ship import Ship
import movement
from pygame.sprite import Group

def main():

    pygame.init()
    display = pygame.display.set_mode((800, 600))
    bg_color = 	(0, 0, 0)
    pygame.display.set_caption("Space Shooters")

    ship = Ship(display)
    bullets = Group()
    display_rect = display.get_rect()

    while True:
        movement.check_events(display, ship, bullets)
        bullets.update()
        ship.updates()
        for bullet in bullets.copy():
            if bullet.rect.right >= display_rect.right:
                bullets.remove(bullet)
        print(len(bullets))
        movement.updateDisplay(display, ship, bg_color, bullets)
        

main()