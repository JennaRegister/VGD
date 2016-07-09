import pygame
import pygame.mixer
import pygame.locals as pl
pygame.mixer.init(44100, -16, 2, 2048)
# pygame.mixer.init()
pygame.init()

screen_width = 800
screen_height = 600

# R, G, B
white = (255, 255, 255)
black = (0, 0, 0)

dimensions = (screen_width, screen_height)
main_surface = pygame.display.set_mode(dimensions)

clock = pygame.time.Clock()
game_exit = False

blockx = screen_width / 2.0
blocky = screen_height / 2.0
blocksize = 20

floor = screen_height - 50

mysound = pygame.mixer.Sound("sounds/plink_lo.wav")

vy = 0.0
vx = 0.0
gravity = 1.0
bounciness = .9

main_surface.fill(white)

while not game_exit:

    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True

    vy += gravity
    blocky += vy
    blockx += vx

    if blocky + blocksize > floor:
        blocky = floor - blocksize
        vy *= -bounciness
        mysound.play()

    main_surface.fill(white)
    pygame.draw.line(main_surface, black, (0, floor), (screen_width, floor))
    pygame.draw.rect(main_surface, black, (blockx, blocky, blocksize, blocksize))

    pygame.display.update()

    clock.tick(60)

print("bye!")
pygame.quit()