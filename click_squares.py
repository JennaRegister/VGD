import pygame
import pygame.locals as pl
pygame.init()
import random
from vgd import random_color

screen_width = 800
screen_height = 600

# R, G, B
white = (255, 255, 255)
black = (0, 0, 0)

main_surface = pygame.display.set_mode((screen_width, screen_height))

game_exit = False

side_length = 30

objects = []









def create_square_centered_at(center, size, color):
    mid_x, mid_y = center

    left = mid_x - size / 2
    top = mid_y - size / 2

    vx = random.randint(-3,3)
    vy = random.randint(-3,3)
    return { "rect": [left, top, size, size], "color": color, "velocity": [vx,vy]}









def draw_object(obj):
    pygame.draw.rect(main_surface, obj["color"], obj["rect"])

def move_object(obj):
    obj["rect"][0] += obj["velocity"][0]
    obj["rect"][1] += obj["velocity"][1]

# main loop over frames
while not game_exit:

    # handle input
    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True
        elif evt.type == pl.MOUSEBUTTONUP:
            new_square = create_square_centered_at(evt.pos, side_length, random_color())
            objects.append(new_square)

    # draw frame
    main_surface.fill(white)
    for obj in objects:
        move_object(obj)
        draw_object(obj)

    # update screen
    pygame.display.update()

pygame.quit()