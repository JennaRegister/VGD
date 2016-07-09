import pygame
import pygame.time
import pygame.locals as pl
from puck_physics import Puck, PuckSet
import math, random
from vgd_advanced import colors, check_quit, random_color, random_velocity, coordinate_rotation
pygame.init()

screen_width = 800
screen_height = 600

main_surface = pygame.display.set_mode((screen_width, screen_height))

paused = False

puckset = PuckSet()

def draw_frame():
    main_surface.fill(colors['white'])
    puckset.draw_all(main_surface)

    # show results
    pygame.display.update()

screen_rect = main_surface.get_rect()

CIRCLE_SPEED = 8
PUCK_BOUNCINESS = 1.0
WALL_BOUNCINESS = 0.8
GRAVITY = pygame.math.Vector2(0,0.5)

clock = pygame.time.Clock()

game_exit = False

while not game_exit:

    game_exit = check_quit()

    # Handle inputs
    for evt in pygame.event.get():
        if evt.type == pl.MOUSEBUTTONUP:
            dir = random.random() * 2 * math.pi
            new_puck = Puck(evt.pos, (math.cos(dir)*CIRCLE_SPEED, math.sin(dir)*CIRCLE_SPEED), random_color(), 10)
            puckset.add(new_puck)

    # move and draw all the circles
    if not paused:
        puckset.drift(GRAVITY)
        puckset.friction(0.98)
        puckset.update_all(PUCK_BOUNCINESS, screen_rect, WALL_BOUNCINESS)

    draw_frame()

    clock.tick(60)

pygame.quit()