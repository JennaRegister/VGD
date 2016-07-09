import pygame
import pygame.time
pygame.init()
from vgd import check_quit

screen_width = 800
screen_height = 600

# R, G, B
white = (255, 255, 255)
black = (0, 0, 0)

main_surface = pygame.display.set_mode((screen_width, screen_height))

game_exit = False

blocksize = 20
blockx = 0
blocky = screen_height / 2 - blocksize / 2

print("fill")
main_surface.fill(white)

print("up")
pygame.display.update()

last_time = pygame.time.get_ticks()

while not game_exit:

    game_exit = check_quit()

    pygame.draw.rect(main_surface, white, (blockx, blocky, blocksize, blocksize))
    blockx += 4
    pygame.draw.rect(main_surface, black, (blockx, blocky, blocksize, blocksize))

    # move the block and draw it in it's new position
    pygame.display.update((blockx-4, blocky, blocksize+4, blocksize))

    now = pygame.time.get_ticks()
    print(int(1000.0 / (now - last_time)))
    last_time = now

pygame.quit()