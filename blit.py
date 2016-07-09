import pygame
pygame.init()
from vgd import colors#wait_until_quit


screen_width = 300
screen_height = 200

main_surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("blitting")

main_surface.fill(colors["white"])


other_surface = pygame.Surface((100,30)).convert_alpha()
other_surface.fill(colors["red"])
other_surface.fill((0,0,0,0), rect=(40,12,20,6))

main_surface.blit(other_surface, (0,0,100,30))
main_surface.blit(other_surface, (150,150,100,30))


pygame.display.update()
#wait_until_quit()
pygame.quit()
