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
o_speed = 0
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
    ball_move(ball, W, H, player, opponent)

