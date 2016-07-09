import pygame
import pygame.mixer
import pygame.time
import pygame.font
import pygame.locals as pl
import random, math
from vgd import colors
pygame.init()
pygame.font.init()
pygame.mixer.init(44100, -16, 2, 2048)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 120
PADDLE_SPEED = 6
BALL_SPEED = 10
BALL_SIZE = 10
FONT_SIZE = 30
SCALE_BOUNCE_EFFECT = 30.0

main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_exit = False

# each player and the ball are represented by rectangles
player_1_rect = [0, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT]
player_2_rect = [SCREEN_WIDTH-PADDLE_WIDTH, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT]
ball_rect = [SCREEN_WIDTH/2-BALL_SIZE/2, SCREEN_HEIGHT/2-BALL_SIZE/2, BALL_SIZE, BALL_SIZE]
# ball_vel[0] is vx, ball_vel[1] is vy
ball_vel = [0,0]

plink = pygame.mixer.Sound("sounds/plink.wav")
plink_lo = pygame.mixer.Sound("sounds/plink_lo.wav")
reward = pygame.mixer.Sound("sounds/reward.wav")

music_loaded = False
music_started = False
music_playing = False
def play_music():
    global music_loaded, music_started
    pygame.mixer.music.set_volume(0.3)
    if not music_loaded:
        pygame.mixer.music.load("sounds/trillek-theme.wav")
        music_loaded = True

    if music_started:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.play(-1)
        music_started = True

def toggle_music():
    global music_playing
    if music_playing:
        pygame.mixer.music.pause()
        music_playing = False
    else:
        play_music()
        music_playing = True

player_1_score = 0
player_2_score = 0

text_renderer = pygame.font.Font(None, FONT_SIZE)
def update_score_text_objects():
    global p1_score_text, p2_score_text, p1_score_rect, p2_score_rect
    p1_score_text = text_renderer.render(str(player_1_score), True, colors["white"])
    p2_score_text = text_renderer.render(str(player_2_score), True, colors["white"])
    p1_score_rect = p1_score_text.get_rect()
    p2_score_rect = p2_score_text.get_rect()
    p2_score_rect[0] = SCREEN_WIDTH - p2_score_rect[2]

def restart_ball_right():
    global ball_rect, ball_vel
    ball_rect = [SCREEN_WIDTH/2-BALL_SIZE/2, SCREEN_HEIGHT/2-BALL_SIZE/2, BALL_SIZE, BALL_SIZE]

    ball_angle = random.random() * math.pi / 2 - math.pi/4
    ball_vel = [BALL_SPEED*math.cos(ball_angle), BALL_SPEED*math.sin(ball_angle)]

def restart_ball_left():
    global ball_vel
    restart_ball_right()
    ball_vel[0] *= -1

def ball_offset_from_paddle_center(ball_rect, paddle_rect):
    center_ball = ball_rect[1] + ball_rect[3]/2
    center_paddle = paddle_rect[1] + paddle_rect[3] / 2
    dist = center_ball-center_paddle

    # returns distance of center paddle to center ball, or None if missed
    if abs(dist) < paddle_rect[3]/2:
        return dist
    else:
        return None


# leave space at the top for scores
game_rect = [0, FONT_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT-FONT_SIZE]

# initialize ball
if random.randint(0,1) == 0:
    restart_ball_right()
else:
    restart_ball_left()
# initialize text
update_score_text_objects()

# start with music playing
toggle_music()

opportunity_to_hit = True

clock = pygame.time.Clock()
while not game_exit:

    for evt in pygame.event.get():
        if evt.type == pl.QUIT:
            game_exit = True
        if evt.type == pl.KEYUP:
            if evt.key == pl.K_m:
                toggle_music()

    # KEYBOARD CONTROLS
    keys = pygame.key.get_pressed()
    if keys[pl.K_DOWN]:
        player_2_rect[1] += PADDLE_SPEED
    if keys[pl.K_UP]:
        player_2_rect[1] -= PADDLE_SPEED
    if keys[pl.K_s]:
        player_1_rect[1] += PADDLE_SPEED
    if keys[pl.K_w]:
        player_1_rect[1] -= PADDLE_SPEED

    # KEEP PADDLES ON SCREEN
    if player_2_rect[1] > SCREEN_HEIGHT - PADDLE_HEIGHT:
        player_2_rect[1] = SCREEN_HEIGHT - PADDLE_HEIGHT
    elif player_2_rect[1] < game_rect[1]:
        player_2_rect[1] = game_rect[1]

    if player_1_rect[1] > SCREEN_HEIGHT - PADDLE_HEIGHT:
        player_1_rect[1] = SCREEN_HEIGHT - PADDLE_HEIGHT
    elif player_1_rect[1] < game_rect[1]:
        player_1_rect[1] = game_rect[1]

    # MOVE THE BALL
    ball_rect[0] += ball_vel[0]
    ball_rect[1] += ball_vel[1]

    # BOUNCE THE BALL
    # bounce top
    if ball_rect[1] < game_rect[1]:
        ball_vel[1] *= -1
        plink.play()
    # bounce bottom
    elif ball_rect[1] + BALL_SIZE > game_rect[1] + game_rect[3]:
        ball_vel[1] *= -1
        plink.play()

    # past paddle left?
    if ball_rect[0] < PADDLE_WIDTH:
        # check if hitting paddle
        paddle_hit_offset = ball_offset_from_paddle_center(ball_rect, player_1_rect)
        if paddle_hit_offset is not None:
            ball_vel[0] *= -1
            ball_vel[1] += paddle_hit_offset / SCALE_BOUNCE_EFFECT
            plink_lo.play()
        # if not, check if hit wall yet (p2 scored point)
        elif ball_rect[0] <= 0:
            player_2_score += 1
            update_score_text_objects()
            reward.play()
            restart_ball_right()

    # past paddle right?
    if ball_rect[0] + BALL_SIZE > SCREEN_WIDTH - PADDLE_WIDTH:
        # check if hitting paddle
        paddle_hit_offset = ball_offset_from_paddle_center(ball_rect, player_2_rect)
        if paddle_hit_offset is not None:
            ball_vel[0] *= -1
            ball_vel[1] += paddle_hit_offset / SCALE_BOUNCE_EFFECT
            plink_lo.play()
        # if not, check if hit wall yet (p2 scored point)
        elif ball_rect[0] + BALL_SIZE >= SCREEN_WIDTH:
            player_1_score += 1
            update_score_text_objects()
            reward.play()
            restart_ball_left()

    # DRAW FRAME
    main_surface.fill(colors["black"])
    pygame.draw.rect(main_surface, colors["white"], game_rect, 1)
    pygame.draw.rect(main_surface, colors["green"], player_1_rect)
    pygame.draw.rect(main_surface, colors["green"], player_2_rect)
    pygame.draw.rect(main_surface, colors["yellow"], ball_rect)
    main_surface.blit(p1_score_text, p1_score_rect)
    main_surface.blit(p2_score_text, p2_score_rect)

    pygame.display.update()

    clock.tick(60)


pygame.quit()