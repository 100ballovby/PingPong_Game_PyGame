import sys
import pygame as pg


def ball_move(obj, s_with, s_height, pl, opp):
    global speed_x, speed_y  # объявляю переменные speed_x и speed_y из глобального пространства имен ГЛОБАЛЬНЫМИ для функции в тч
    obj.x += speed_x
    obj.y += speed_y

    if obj.top <= 0 or obj.bottom >= s_height:
        speed_y *= -1
    elif obj.left <= 0 or obj.right >= s_with:
        speed_x *= -1
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
o_speed = speed * 0.7
ball_moving = False
speed_x = speed_y = speed

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

