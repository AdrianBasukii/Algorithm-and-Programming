import pygame
import sys
from bullets import Bullet

def keyPressed(event, screen, ship, bullets):
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(screen, ship)
        bullets.add(new_bullet)

def keyReleased(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            keyPressed(event, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            keyReleased(event, ship)

def updateDisplay(display, ship, bg_color, bullets):
    display.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()