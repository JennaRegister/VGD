import pygame
import pygame.locals as pl
import random
pygame.init()
from vgd import colors, is_point_in_rect

screen_width = 800
screen_height = 600

main_surface = pygame.display.set_mode((screen_width, screen_height))

blocksize = 80

nblocks = 500

blocks = [None] * nblocks

for i in range(nblocks):
    # x, y, w, h, vx, vy
    blocks[i] = [random.randint(50, screen_width-50), # x
                 random.randint(50, screen_height-50), #y
                 random.randint(10,50), # w
                 random.randint(10,50), # h
                 random.randint(-5,5), # vx
                 random.randint(-5,5)] # vy

mouse_position = (0,0)

main_surface.fill(colors["white"])

game_exit = False

while not game_exit:


    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True
        elif evt.type == pl.MOUSEMOTION:
            mouse_position = evt.pos

    for block in blocks:
        bx = block[0]
        by = block[1]
        bw = block[2]
        bh = block[3]
        bvx = block[4]
        bvy = block[5]

        block[0] += bvx
        # block[1] += bvy

        if bx > screen_width - bw:
            block[0] = screen_width - bw
            block[4] *= -1
        elif bx < 0:
            block[0] = 0
            block[4] *= -1


    main_surface.fill(colors["white"])
    for block in blocks:

        if is_point_in_rect(mouse_position, block):
            pygame.draw.rect(main_surface, colors['red'], block[0:4])
        else:
            pygame.draw.rect(main_surface, colors['green'], block[0:4])

    pygame.display.update()

pygame.quit()