import pygame
import pygame.mixer
import pygame.locals as pl
pygame.init()
pygame.mixer.init()
from vgd import colors

screen_width = 800
screen_height = 600

main_surface = pygame.display.set_mode((screen_width, screen_height))

game_exit = False

powerup_sound = pygame.mixer.Sound("sounds/powerup.wav")

while not game_exit:

    # handle inputs
    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True
        if evt.type == pl.MOUSEBUTTONUP:
            powerup_sound.play()

    pygame.display.update()

pygame.quit()