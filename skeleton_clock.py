import pygame
import pygame.time
import pygame.locals as pl
pygame.init()
from vgd import colors

screen_width = 800
screen_height = 600

main_surface = pygame.display.set_mode((screen_width, screen_height))

game_exit = False

clock = pygame.time.Clock()


# DEFINE FUNCTIONS AND VARIABLES HERE


while not game_exit:

    # handle inputs
    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True
        # ADD YOUR INPUT CODE HERE

    # DRAW A NEW FRAME HERE

    pygame.display.update()

    clock.tick(60)

pygame.quit()