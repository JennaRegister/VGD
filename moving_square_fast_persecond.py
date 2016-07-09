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

pixels_per_frame = 4.0
frames_per_second = 60.0
pixels_per_second = pixels_per_frame * frames_per_second

main_surface.fill(white)
pygame.display.update()

last_frame_seconds = pygame.time.get_ticks() / 1000.0

while not game_exit:

    game_exit = check_quit()

    # cover up last one
    pygame.draw.rect(main_surface, white, (blockx, blocky, blocksize, blocksize))

    # move the block and draw it in it's new position
    now = pygame.time.get_ticks() / 1000.0
    blockx += (now - last_frame_seconds) * pixels_per_second

    pygame.draw.rect(main_surface, black, (blockx, blocky, blocksize, blocksize))
    pygame.display.update(pygame.Rect(blockx-4, blocky, blocksize+4, blocksize))

    last_frame_seconds = now

    fps()


pygame.quit()