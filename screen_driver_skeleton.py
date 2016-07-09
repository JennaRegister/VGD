import pygame
import pygame.time
import pygame.locals as pl
from screens import ScreenManager
pygame.init()
from vgd import colors

screen_width = 800
screen_height = 600

main_surface = pygame.display.set_mode((screen_width, screen_height))

game_exit = False

clock = pygame.time.Clock()

# CREATE SCREEN OBJECTS HERE

menu_screen = MenuScreen()
pause_screen = PauseScreen()
# ...you define your own class PauseScreen(BaseScreen) and class MenuScreen(BaseScreen), etc..

mgr = ScreenManager()

# for each of your screens, do this:
menu_screen.set_manager(mgr)
pause_screen.set_manager(mgr)

# start the first active screen
mgr.activate("MainMenu")

while not game_exit:

    # handle inputs
    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True
        else:
            mgr.handle_input(evt)

    mgr.update(main_surface)
    mgr.draw()
    pygame.display.update()

    clock.tick(60)

pygame.quit()