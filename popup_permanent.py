import pygame
pygame.init()
from vgd import wait_until_quit

screen_width = 800
screen_height = 600

black = (0,0,0)

main_surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Title goes here")

main_surface.fill((255,255,100))

pygame.draw.rect(main_surface, black, (screen_width,screen_height,30,40))

pygame.display.update()

wait_until_quit()

pygame.quit()
