import pygame
import pygame.time
import pygame.locals as pl
pygame.init()
from vgd import colors

screen_width = 800
screen_height = 600

main_surface = pygame.display.set_mode((screen_width, screen_height))

game_exit = False

clock = pygame.time.Clock()

mm_image = pygame.image.load("images/megaman.png").convert_alpha()

bgcolor = colors["gray"]

while not game_exit:

    # handle inputs
    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True

    mm_image = pygame.transform.rotate(mm_image, 1)
    mm_image_rect = mm_image.get_rect()
    mm_image_rect.centerx = screen_width / 2
    mm_image_rect.centery = screen_height / 2

    main_surface.fill(colors["white"])
    main_surface.blit(mm_image, mm_image_rect)

    pygame.display.update()

    clock.tick(60)

pygame.quit()