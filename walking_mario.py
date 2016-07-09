import pygame
import pygame.time
import pygame.locals as pl
pygame.init()
from vgd import colors, random_color

screen_width = 800
screen_height = 600

main_surface = pygame.display.set_mode((screen_width, screen_height))

marios_surface = pygame.image.load("images/marios.png")

game_exit = False

clock = pygame.time.Clock()

def get_mario_at(row, col):
    # you give me row, col, and i'll tell you the rect [x,y,w,h] of the mario at that row and col
    return [28 * col, 40 * row, 28, 40]

mario_position_left_1 = get_mario_at(1,0)
mario_position_left_2 = get_mario_at(1,1)
mario_position_left_3 = get_mario_at(1,2)
mario_position_left_4 = get_mario_at(1,1)

mario_position_right_1 = get_mario_at(2,0)
mario_position_right_2 = get_mario_at(2,1)
mario_position_right_3 = get_mario_at(2,2)
mario_position_right_4 = get_mario_at(2,1)

all_mario_positions_left = {
    1 : mario_position_left_1,
    2 : mario_position_left_2,
    3 : mario_position_left_3,
    4 : mario_position_left_4,
}

all_mario_positions_right = {
    1 : mario_position_right_1,
    2 : mario_position_right_2,
    3 : mario_position_right_3,
    4 : mario_position_right_4,
}

frames_per_image = 10

position_on_screen = [screen_width/2, screen_height/2, 28, 40]

mario_direction = 1

pose_number = 1 # 1,2,3,4,1,2,3,4,1,2,3,4

frame_counter = 0

while not game_exit:

    frame_counter = frame_counter + 1

    if frame_counter is frames_per_image:
        pose_number = pose_number + 1

        if pose_number is 5:
            pose_number = 1

        frame_counter = 0

    main_surface.fill( colors["white"] )

    # handle inputs
    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True
        if evt.type == pl.KEYDOWN:
            if evt.key == pl.K_RIGHT or evt.key == pl.K_LEFT:
                pose_number = 1
                frame_counter = 0

    keys = pygame.key.get_pressed()
    if keys[pl.K_RIGHT]:
        mario_direction = 1
        position_on_screen[0] += 2
    elif keys[pl.K_LEFT]:
        position_on_screen[0] -= 2
        mario_direction = -1
    else:
        pose_number = 2

    if mario_direction == 1:
        main_surface.blit(marios_surface, position_on_screen, all_mario_positions_right[pose_number])
    else:
        main_surface.blit(marios_surface, position_on_screen, all_mario_positions_left[pose_number])

    pygame.display.update()

    clock.tick(60)

pygame.quit()