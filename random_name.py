import pygame
import pygame.font as f
import pygame.locals as pl
import random
from vgd import colors
pygame.init()
f.init()

# names = ["Caleb", "Noah", "Desmond", "Philip", "Jalon", "Daniel", "Chris", "Tim", "Alaul", "Kaylyn", "Alex", "Jiaqi", "Jeff", "Dane", "Ricardo" ]
names = ["Chris", "Kaylyn", "Jalon", "Alaul", "Dane", "Caleb", "Ricardo"]
counts = [1.0] * len(names)

screen_width = 300
screen_height = 100

main_surface = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("")

BACKGROUND = colors["white"]

text_maker = f.Font("fonts/Roboto-Regular.ttf", 40)

def weighted_random(weights):
    tot = sum(weights)
    num = random.random() * tot

    running = 0

    for i in range(1,len(weights)):
        running += weights[i]
        if num < running:
            return i
    return len(weights) - 1

def new_name():
    choice = weighted_random([1.0 / c for c in counts])
    counts[choice] += 10.0
    text = text_maker.render(names[choice], 1, colors["black"])
    text_rect = text.get_rect()
    text_rect.centerx = main_surface.get_rect().centerx
    text_rect.centery = main_surface.get_rect().centery

    # draw it
    main_surface.fill(BACKGROUND)
    main_surface.blit(text, text_rect)

    pygame.display.update()

quit = False

while not quit:

    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            quit = True
        if evt.type == pl.MOUSEBUTTONUP:
            new_name()

