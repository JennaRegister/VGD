import pygame
import pygame.locals as pl
pygame.init()
from vgd import colors

screen_width = 800
screen_height = 600

main_surface = pygame.display.set_mode((screen_width, screen_height))


# Helper functions
def create_square_centered_at(center, size, color):
    mid_x, mid_y = center

    left = mid_x - size / 2
    top = mid_y - size / 2

    # Using a LIST "[]" for the rect rather than a TUPLE "()" because lists allow things to be changed in-place
    return { "rect": [left, top, size, size], "color": color }

def draw_square(square):
    pygame.draw.rect(main_surface, square["color"], square["rect"])

def move_square(square, dx, dy):
    square["rect"][0] += dx
    square["rect"][1] += dy


def contain(square, boundary_rect):
    r = square["rect"]
    # Left check
    if r[0] < boundary_rect[0]:
        r[0] = boundary_rect[0]
    # Right check
    elif r[0] + r[2] > boundary_rect[0] + boundary_rect[2]:
        # set to boundary - width of square
        r[0] = boundary_rect[2] - r[2]

    # Top check
    # WHAT IF THIS WERE 'elif'???
    if r[1] < boundary_rect[1]:
        r[1] = boundary_rect[1]
    # bottom check
    elif r[1] + r[3] > boundary_rect[1] + boundary_rect[3]:
        # set to boundary - height of square
        r[1] = boundary_rect[3] - r[3]

# variables

side_length = 20
movement = 5
the_square = create_square_centered_at((screen_width/2, screen_height/2), side_length, colors["black"])

# main loop
game_exit = False
while not game_exit:

    # handle inputs
    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True

    keys = pygame.key.get_pressed()
    if keys[pl.K_DOWN]:
        move_square(the_square, 0, movement)
    if keys[pl.K_UP]:
        move_square(the_square, 0, -movement)
    if keys[pl.K_LEFT]:
        move_square(the_square, -movement, 0)
        print("got it!") + str(movement)
    if keys[pl.K_RIGHT]:
        move_square(the_square, movement, 0)

    # keep it on the screen
    contain(the_square, main_surface.get_rect())

    main_surface.fill(colors["white"])
    draw_square(the_square)

    pygame.display.update()

pygame.quit()
