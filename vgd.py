import pygame
import pygame.time
import pygame.mixer
import pygame.locals as pl
import random
pygame.init()
pygame.mixer.init()

colors = {
    "black": (0,0,0),
    "white": (255,255,255),
    "red": (255,0,0),
    "green": (0,255,0),
    "dark-green": (0,200,0),
    "blue": (0,0,255),
    "gray": (100,100,100),
    "yellow": (255,255,0),
    "orange": (255,100,0),
    "purple": (200, 0, 255)
}

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)


def is_point_in_rect(point, rect):
    pos_x = point[0]
    pos_y = point[1]

    rect_left   = rect[0]
    rect_top    = rect[1]
    rect_width  = rect[2]
    rect_height = rect[3]

    rect_right = rect_left + rect_width
    rect_bottom = rect_top + rect_height

    return pos_x >= rect_left and pos_x <= rect_right and pos_y >= rect_top and pos_y <= rect_bottom


__loaded_sounds = {}
def load_and_play_sound(path):
    global __loaded_sounds

    if path not in __loaded_sounds:
            __loaded_sounds[path] = pygame.mixer.Sound(path)

    __loaded_sounds[path].play()


__last_millis = None
def fps():
    global __last_millis

    now = pygame.time.get_ticks()

    if __last_millis is not None:
        fps = int(1000.0 / (now - __last_millis))
        print(fps)

    __last_millis = now