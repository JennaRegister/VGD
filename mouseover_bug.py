import pygame
import pygame.locals as pl
pygame.init()
from vgd import colors, is_point_in_rect

screen_width = 800
screen_height = 600

main_surface = pygame.display.set_mode((screen_width, screen_height))

blocksize = 80

block = (screen_width/2-blocksize/2, screen_height/2-blocksize/2, blocksize, blocksize)

main_surface.fill(colors["white"])

game_exit = False

while not game_exit:

    the_color = colors["green"]

    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True
        elif evt.type == pl.MOUSEMOTION:
            if is_point_in_rect(evt.pos, block):
                the_color = colors["red"]

    pygame.draw.rect(main_surface, the_color, block)

    pygame.display.update()

pygame.quit()