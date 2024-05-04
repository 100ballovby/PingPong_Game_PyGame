import sys
import pygame as pg
from random import choice


def restart(obj, s_width, s_height, s):
    global speed_x, speed_y, score_time
    obj.center = (s_width // 2, s_height // 2)
    speed_x *= choice([-1, 1])
    speed_y *= choice([-1, 1])

    cur_time = pg.time.get_ticks()
    if cur_time - score_time < 700:
        num_3 = score_font.render('3', True, BLUE)
        screen.blit(num_3, [s_width // 2, s_height // 2])
    elif cur_time - score_time < 1400:
        num_2 = score_font.render('2', True, BLUE)
        screen.blit(num_2, [s_width // 2, s_height // 2])
    elif cur_time - score_time < 2100:
        num_1 = score_font.render('1', True, BLUE)
        screen.blit(num_1, [s_width // 2, s_height // 2])

    if cur_time - score_time < 2100:
        speed_x, speed_y = 0, 0
    else:
        speed_x = s * choice([-1, 1])
        speed_y = s * choice([-1, 1])
        score_time = None  # выключаем триггер


def ball_move(obj, s_with, s_height, pl, opp):
    global speed_x, speed_y, p_score, o_score, score_time  # объявляю переменные speed_x и speed_y из глобального пространства имен ГЛОБАЛЬНЫМИ для функции в тч
    obj.x += speed_x
    obj.y += speed_y

    if obj.top <= 0 or obj.bottom >= s_height:
        speed_y *= -1
    elif obj.left <= 0:
        score_time = pg.time.get_ticks()  # фиксация "времени", когда был забит гол
        p_score += 1
    elif obj.right >= s_with:
        score_time = pg.time.get_ticks()  # фиксация "времени", когда был забит гол
        o_score += 1
    elif obj.colliderect(pl) or obj.colliderect(opp):
        speed_x *= -1


def player_move(pl, s, s_height):
    pl.y += s
    if pl.top <= 0:
        pl.top = 0
    elif pl.bottom >= s_height:
        pl.bottom = s_height


def opponent_motion(op, ball_obj, s, s_height):
    if op.top < ball_obj.y:
        op.y += s
    elif op.bottom > ball_obj.y:
        op.y -= s

    if op.top <= 0:
        op.top = 0
    elif op.bottom >= s_height:
        op.bottom = s_height


W = 1280
H = 720
FPS = 60
clock = pg.time.Clock()

# COLORS
GREEN = (138, 191, 126)
WHITE = (255, 255, 255)
BLUE = (109, 124, 191)

# playable objects
player = pg.Rect(0, 0, 15, 150)
opponent = pg.Rect(0, 0, 15, 150)
ball = pg.Rect(0, 0, 30, 30)

player.center = (W - 15, H // 2)
opponent.center = (15, H // 2)
ball.center = (W // 2, H // 2)

# game config
speed = 7
p_speed = 0
o_speed = speed * 0.8
ball_moving = False
speed_x = speed * choice([-1, 1])
speed_y = speed * choice([-1, 1])
score_time = True

p_score, o_score = 0, 0
pg.font.init()
score_font = pg.font.SysFont('comicsans', 64)

pg.init()  # инициализируем pygame
screen = pg.display.set_mode((W, H))  # создаем экран игры разрешением 1280х720px
pg.display.set_caption('Ping Pong | PyGame')

while True:  # цикл игры
    clock.tick(FPS)
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill(GREEN)
    pg.draw.rect(screen, BLUE, player)
    pg.draw.rect(screen, BLUE, opponent)
    pg.draw.aaline(screen, WHITE, [W // 2, 0], [W // 2, H])
    pg.draw.ellipse(screen, BLUE, ball)

    p_score_text = score_font.render(str(p_score), True, BLUE)
    o_score_text = score_font.render(str(o_score), True, BLUE)
    screen.blit(p_score_text, [W // 2 + 50, H * 0.25])
    screen.blit(o_score_text, [W // 2 - 85, H * 0.25])

    if score_time:
        restart(ball, W, H, speed)

    pg.display.update()

    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        p_speed = -speed
    elif keys[pg.K_DOWN]:
        p_speed = speed
    else:
        p_speed = 0

    ball_move(ball, W, H, player, opponent)
    player_move(player, p_speed, H)
    opponent_motion(opponent, ball, o_speed, H)

