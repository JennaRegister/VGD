import pygame
pygame.init()
from vgd import check_quit

screen_width = 800
screen_height = 600

# R, G, B
white = (255, 255, 255)
black = (0, 0, 0)

dimensions = (screen_width, screen_height)
main_surface = pygame.display.set_mode(dimensions)

clock = pygame.time.Clock()
game_exit = False

blockx = screen_width / 2
blocky = screen_height / 2
blocksize = 20

vx = 5

main_surface.fill(white)

while not game_exit:

    game_exit = check_quit()

    blockx += vx

    if blockx <= 0 or blockx + blocksize >= screen_width:
        vx *= -1

    main_surface.fill(white)
    pygame.draw.rect(main_surface, black, (blockx, blocky, blocksize, blocksize))

    pygame.display.update()

    clock.tick(60)

print("bye!")
pygame.quit()