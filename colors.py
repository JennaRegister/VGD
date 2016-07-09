import pygame
pygame.init()
from vgd import wait_until_quit

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gray = (100,100,100)
yellow = (255,255,0)
orange = (255,100,0)
purple = (200, 0, 255)

screen_width = 800
screen_height = 600

main_surface = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("colors")

def draw_colored_squares(colors_array, square_width):

    # find the center of the screen
    middle_x = screen_width / 2

    # find the total width of having all the blocks next to each other
    number_of_squares = len(colors_array)
    total_width = number_of_squares * square_width

    # if all of the squares side by side take up total_width space, then the farthest left one
    # should start at middle_x - total_width / 2
    x = middle_x - total_width / 2

    # in the loop, we do the following:
    #   draw each color at position x
    #   move x to the right by 1 width of the square
    for color in colors_array:
        pygame.draw.rect(main_surface, color, (x, screen_height/2, square_width, square_width))
        x = x + square_width

# fill the background
main_surface.fill(white)

# draw all the squares
draw_colored_squares([red,green,blue,orange,yellow,purple,gray], 30)

# show the results
pygame.display.update()

wait_until_quit()

pygame.quit()