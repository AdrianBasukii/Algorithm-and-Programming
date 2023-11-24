import sys
import pygame

def main():

    pygame.init()
    display = pygame.display.set_mode((800, 600))
    bg_color = 	(0, 0, 0)
    pygame.display.set_caption("Test")
    image = pygame.image.load('Images/star.bmp')
    image_rect = image.get_rect()
    image_rectx = image_rect.width
    image_recty = image_rect.height
    x = float(image_rectx)
    display_rect = display.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        display.blit(image, image_rect)

main()
        