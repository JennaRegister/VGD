import pygame
import pygame.time
import pygame.mixer
import pygame.locals as pl
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
from buttons import Button
from vgd import colors

screen_width = 800
screen_height = 600

main_surface = pygame.display.set_mode((screen_width, screen_height))

screen_rect = main_surface.get_rect()

game_exit = False

clock = pygame.time.Clock()

mysound = pygame.mixer.Sound("sounds/plink.wav")

bg_music_file = "sounds/trillek-theme.wav"

pygame.mixer.music.load(bg_music_file)
started_playing = False
def play_music():
    global started_playing
    if not started_playing:
        pygame.mixer.music.play()
        started_playing = True
    else:
        pygame.mixer.music.unpause()

def pause_music():
    pygame.mixer.music.pause()

plink_btn = Button("click for sound",
             (screen_rect.centerx, screen_rect.centery), mysound.play,
             20, colors["green"], colors["black"], colors["gray"], 5)
music_play_btn = Button("play music",
             (screen_rect.centerx, screen_rect.centery+25), play_music,
             20, colors["green"], colors["black"], colors["gray"], 5)
music_pause_btn = Button("pause music",
             (screen_rect.centerx, screen_rect.centery+50), pause_music,
             20, colors["green"], colors["black"], colors["gray"], 5)

while not game_exit:

    # handle inputs
    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True
        if evt.type == pl.MOUSEBUTTONUP:
            plink_btn.handle_mouseup_event(evt)
            music_play_btn.handle_mouseup_event(evt)
            music_pause_btn.handle_mouseup_event(evt)

    main_surface.fill(colors["white"])
    plink_btn.render(main_surface, pygame.mouse.get_pos())
    music_play_btn.render(main_surface, pygame.mouse.get_pos())
    music_pause_btn.render(main_surface, pygame.mouse.get_pos())

    pygame.display.update()

    clock.tick(60)

pygame.quit()