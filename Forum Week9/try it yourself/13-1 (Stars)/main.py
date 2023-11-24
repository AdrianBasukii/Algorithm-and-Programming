import sys
import pygame

def main():

    pygame.init()
    display = pygame.display.set_mode((800, 600))
    bg_color = 	(0, 0, 0)
    pygame.display.set_caption("Space Shooters")

    display_rect = display.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

main()