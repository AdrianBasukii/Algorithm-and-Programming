import sys
import pygame
from rocket import Rocket
import movement

def main():

    pygame.init()
    display = pygame.display.set_mode((800, 600))
    bg_color = 	(229, 229, 229)
    pygame.display.set_caption("R O C K E T")

    rocket = Rocket(display)

    while True:
        movement.check_events(rocket)
        rocket.updates()
        movement.updateDisplay(display, rocket, bg_color)

main()