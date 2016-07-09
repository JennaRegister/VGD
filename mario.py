import pygame
import pygame.time
import pygame.locals as pl
pygame.init()

screen_width = 400
screen_height = 300

main_surface = pygame.display.set_mode((screen_width, screen_height))

marios = pygame.image.load("images/marios.png")

game_exit = False

clock = pygame.time.Clock()

MARIO_WIDTH = 28
MARIO_HEIGHT = 40

walk_cycle = 0
walk_freqency = 12 # change every 10 frames

def get_mario_at(row, col):
    return [col*MARIO_WIDTH, row*MARIO_HEIGHT, MARIO_WIDTH, MARIO_HEIGHT]

dest_rect = [screen_width / 2 - MARIO_WIDTH / 2, screen_height / 2 - MARIO_HEIGHT / 2, MARIO_WIDTH, MARIO_HEIGHT]

bgcolor = (100,128,255)

main_surface.fill(bgcolor)


frame_counter = 0
while not game_exit:

    # handle inputs
    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True

    if walk_cycle == 0:
        source_rect = get_mario_at(0,0)
    elif walk_cycle == 1 or walk_cycle == 3:
        source_rect = get_mario_at(0,1)
    elif walk_cycle == 2:
        source_rect = get_mario_at(0,2)


    # BLIT THE MARIO IMAGE
    main_surface.fill(bgcolor, dest_rect)
    main_surface.blit(marios, dest_rect, source_rect)
    pygame.display.update()

    clock.tick(60)

    frame_counter += 1
    if frame_counter == walk_freqency:
        frame_counter = 0
        walk_cycle  = (walk_cycle + 1) % 4

pygame.quit()