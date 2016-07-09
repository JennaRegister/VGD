import pygame
import pygame.locals as pl
import random, math
pygame.init()

colors = {
    "black": (0,0,0),
    "white": (255,255,255),
    "red": (255,0,0),
    "green": (0,255,0),
    "blue": (0,0,255),
    "gray": (100,100,100),
    "yellow": (255,255,0),
    "orange": (255,100,0),
    "purple": (200, 0, 255)
}

def check_quit():
    # pygame.event.peek( type ) tells us whether there is an event of the given type waiting on the queue
    return pygame.event.peek(pl.QUIT)

def wait_until_quit():
    while True:
        if check_quit():
            return

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

def random_velocity(speed):
    # picks a random direction and returns a list [vx, vy] that is motion in that direction at the given speed
    direction = random.random() * math.pi * 2

    vx = math.cos(direction) * speed
    vy = math.sin(direction) * speed

    return [vx, vy]

def coordinate_rotation(x, y, angle):
    s = math.sin(angle)
    c = math.cos(angle)

    new_x = c * x + s * y
    new_y = c * y - s * x

    return [new_x, new_y]