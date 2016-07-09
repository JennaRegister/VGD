import pygame
import pygame.time
import random
import pygame.locals as pl
pygame.init()

from vgd import colors
from classes import BouncingRectangle, BouncingMegaman

screen_width = 800
screen_height = 600

main_surface = pygame.display.set_mode((screen_width, screen_height))

game_exit = False

clock = pygame.time.Clock()

def random_coordinate():
    return (random.randint(0,screen_width), random.randint(0,screen_height))

my_instance_of_br = BouncingRectangle(random_coordinate(), (-3,-3), 15, 30, colors["purple"])
my_instance_of_bmm = BouncingMegaman(random_coordinate(), (-3,-3))

screen_rectangle = main_surface.get_rect()


while not game_exit:
    # handle inputs
    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True


    # call the move function of each one
    my_instance_of_br.move()
    my_instance_of_bmm.move()

    # contain each within the screen
    my_instance_of_br.contain_within_rect(screen_rectangle)
    my_instance_of_bmm.contain_within_rect(screen_rectangle)

    # draw each one
    main_surface.fill(colors["white"])
    my_instance_of_br.draw(main_surface)
    my_instance_of_bmm.draw(main_surface)

    pygame.display.update()

    clock.tick(60)

pygame.quit()