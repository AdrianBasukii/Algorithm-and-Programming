import pygame
import sys

def blue():

    pygame.init()
    display = pygame.display.set_mode((800, 600))
    bg_color = 	(173, 216, 230)
    pygame.display.set_caption("Blue Sky")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        display.fill(bg_color)
        pygame.display.flip()

blue()