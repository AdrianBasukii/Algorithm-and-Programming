import sys
import pygame
from character import Chara

def main():

    pygame.init()
    display = pygame.display.set_mode((800, 600))
    bg_color = 	(33, 33, 33)
    pygame.display.set_caption("Hutao")

    chara = Chara(display)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        display.fill(bg_color)
        chara.blitme()
        pygame.display.flip()

main()