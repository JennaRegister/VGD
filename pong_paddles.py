import pygame
import pygame.time
pygame.init()
from vgd import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game_exit = False

PADDLE_WIDTH = 15
PADDLE_HEIGHT = 120
PADDLE_SPEED = 3

left_paddle_y = SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2
left_paddle_x = 0
right_paddle_y = left_paddle_y
right_paddle_x = SCREEN_WIDTH - PADDLE_WIDTH

clock = pygame.time.Clock()
while not game_exit:

    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True

    # KEYBOARD CONTROLS
    keys = pygame.key.get_pressed()
    if keys[pl.K_DOWN]:
        right_paddle_y += PADDLE_SPEED
    if keys[pl.K_UP]:
        right_paddle_y -= PADDLE_SPEED
    if keys[pl.K_s]:
        left_paddle_y += PADDLE_SPEED
    if keys[pl.K_w]:
        left_paddle_y -= PADDLE_SPEED

    # KEEP ON SCREEN
    if right_paddle_y > SCREEN_HEIGHT - PADDLE_HEIGHT:
        right_paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT
    elif right_paddle_y < 0:
        right_paddle_y = 0

    if left_paddle_y > SCREEN_HEIGHT - PADDLE_HEIGHT:
        left_paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT
    elif left_paddle_y < 0:
        left_paddle_y = 0

    # DRAW FRAME
    main_surface.fill(colors["black"])
    pygame.draw.rect(main_surface, colors["green"], (left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(main_surface, colors["green"], (right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    pygame.display.update()

    clock.tick(60)


pygame.quit()