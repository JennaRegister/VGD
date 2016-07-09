



current_mode = PongGame()


while not game_exit:

    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True
        elif evt.type == pl.KEYUP:
            if evt.key == pl.K_p:
                current_mode = PauseMode()
        else:
            current_mode.handle_event(evt)

    current_mode.update()
    current_mode.draw()
    pygame.display.update()
