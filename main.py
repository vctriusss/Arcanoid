import time
from constants import *
from Platform import Platform
from Ball import Ball
from block_patterns import *

pg.init()
pg.display.set_caption('Arcanoid')
img = pg.image.load('background.jpg')


def EndGameScenario(win: bool):
    black = pg.Rect(int(0.3 * screen_width), int(0.45 * screen_height), 500, 150)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    exit()
                elif event.key == pg.K_r:
                    return True
        pg.draw.rect(screen, pg.Color('black'), black)
        if win:
            screen.blit(text_youwin, (black.x + 10, black.y + 5))
        else:
            screen.blit(text_gameover, (black.x + 10, black.y + 5))
        screen.blit(text_reload, (black.x + 10, black.y + 100))
        pg.display.flip()


def object_collision(obj1, obj2):
    if obj1.body.colliderect(obj2.body):
        delta_x = obj2.body.right - obj1.body.left if obj2.dx > 0 else obj1.body.right - obj2.body.left
        delta_y = obj2.body.bottom - obj1.body.top if obj2.dy > 0 else obj1.body.bottom - obj2.body.top
        # corner hit
        if abs(delta_x - delta_y) < 5:
            obj2.dx *= -1
            obj2.dy *= -1
        # left or right side hit
        elif delta_x > delta_y:
            obj2.dy *= -1
        # top or bottom side hit
        else:
            obj2.dx *= -1
        pg.draw.rect(screen, pg.Color('white'), obj1.body, border_radius=3)
        if type(obj1) == Block:
            block_pattern.remove(obj1)


def draw_objects(*args):
    for arg in args:
        if type(arg) != list:
            arg.draw()
        else:
            for block in arg:
                block.draw()
    pg.display.flip()


def game():
    platform = Platform()
    ball = Ball()
    global block_pattern
    block_pattern = choice(patterns).copy()
    clock = pg.time.Clock()

    time_end = time.time() + 1
    while time.time() < time_end:
        screen.blit(img, (0, 0))
        draw_objects(platform, ball)
        pg.display.flip()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
        key = pg.key.get_pressed()
        if key[pg.K_a] and platform.body.left > 0:
            platform.body.left -= platform.speed
        if key[pg.K_d] and platform.body.right < screen_width:
            platform.body.right += platform.speed
        if key[pg.K_ESCAPE]:
            exit()
        screen.blit(img, (0, 0))

        ball.fly()
        if ball.is_out():
            EndGameScenario(win=False)
            game()
        ball.wall_bounce()
        object_collision(platform, ball)
        for block in block_pattern:
            object_collision(block, ball)
            if len(block_pattern) == 0:
                EndGameScenario(win=True)
                game()
        draw_objects(platform, ball, block_pattern)
        clock.tick(fps)


if __name__ == '__main__':
    game()
