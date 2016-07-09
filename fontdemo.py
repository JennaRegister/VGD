import pygame
import pygame.font
import pygame.locals as pl
pygame.init()
pygame.font.init()

main_surface = pygame.display.set_mode((300,100))

myfont = pygame.font.Font("fonts/Pacifico.ttf", 18)

mytext = myfont.render("Hello World!", True, (0,0,0))
rect = mytext.get_rect()

rect.centerx = main_surface.get_rect().centerx
rect.centery = main_surface.get_rect().centery

# 'mytext' is another Surface. we use 'blit' to copy pixels from it to the screen. To do so, we need to tell
# 'blit' where on the 'main_surface' we want it.

main_surface.fill((255,255,255))
main_surface.blit(mytext, rect)

quit = False

while not quit:
    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            quit = True
    pygame.display.update()