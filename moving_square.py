import pygame
import pygame.locals as pl
pygame.init()
from vgd import colors

screen_width = 800
screen_height = 600

main_surface = pygame.display.set_mode((screen_width, screen_height))

# variables
side_length = 20
blockx = 0
blocky = screen_height/2 - side_length/2

# main loop
game_exit = False
while not game_exit:

    # handle inputs
    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True

    blockx += 4

    main_surface.fill(colors["white"])
    pygame.draw.rect(main_surface, colors["black"], (blockx, blocky, side_length, side_length))

    pygame.display.update()

pygame.quit()