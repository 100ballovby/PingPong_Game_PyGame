import sys
import pygame as pg

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

pg.init()  # инициализируем pygame
screen = pg.display.set_mode((W, H))  # создаем экран игры разрешением 1280х720px
pg.display.set_caption('Ping Pong | PyGame')

while True:  # цикл игры
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
