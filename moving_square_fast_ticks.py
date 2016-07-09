import pygame_sdl2
pygame_sdl2.import_as_pygame()
import pygame
import pygame.time
pygame.init()
from vgd import check_quit, fps

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

clock = pygame.time.Clock()

main_surface.fill(white)
pygame.display.update()

while not game_exit:

    game_exit = check_quit()

    # cover up last one
    pygame.draw.rect(main_surface, white, (blockx, blocky, blocksize, blocksize))

    # move the block and draw it in it's new position
    blockx += 4
    pygame.draw.rect(main_surface, black, (blockx, blocky, blocksize, blocksize))

    pygame.display.update(pygame.Rect(blockx-4, blocky, blocksize+4, blocksize))

    fps()

    clock.tick(60)


pygame.quit()