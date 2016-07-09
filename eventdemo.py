import pygame
import pygame.locals as pl
pygame.init()

screen_width = 800
screen_height = 600

main_surface = pygame.display.set_mode((screen_width, screen_height))

game_exit = False

while not game_exit:

    for evt in pygame.event.get():
        print(evt)
        if evt.type == pl.QUIT:
            game_exit = True

    pygame.display.update()

pygame.quit()
