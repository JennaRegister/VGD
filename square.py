import pygame
pygame.init()
from vgd import wait_until_quit, colors

screen_width = 800
screen_height = 600

main_surface = pygame.display.set_mode((screen_width,screen_height))


main_surface.fill(colors["blue"])

side_length = 120

x = screen_width / 2 - side_length / 2
y = screen_height / 2 - side_length / 2
w = side_length
h = side_length

pygame.draw.rect(main_surface, colors["red"], (x, y, w, h) )

pygame.display.update()

wait_until_quit()