import time
from constants import *
from Platform import Platform
from Ball import Ball
from block_patterns import *
from Bonus import Bonus


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
    if obj1.rect.colliderect(obj2.rect):
        if type(obj1) == Block:
            blocks.remove(obj1)
            bonuses.add(Bonus(obj1))
        delta_x = obj2.rect.right - obj1.rect.left if obj2.dx > 0 else obj1.rect.right - obj2.rect.left
        delta_y = obj2.rect.bottom - obj1.rect.top if obj2.dy > 0 else obj1.rect.bottom - obj2.rect.top
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
        pg.draw.rect(screen, pg.Color('white'), obj1.rect, border_radius=3)


def draw_objects(*args):
    for arg in args:
        if type(arg) != pg.sprite.Group():
            screen.blit(arg.image, arg.rect)
        else:
            for block in arg:
                screen.blit(block.image, block.rect)
    pg.display.flip()


def game():
    pg.init()
    platform = Platform()
    ball = Ball()
    global block_pattern, blocks, bonuses
    block_pattern = choice(patterns).copy()
    blocks = pg.sprite.Group()
    bonuses = pg.sprite.Group()
    for b in block_pattern:
        blocks.add(b)
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
        if key[pg.K_a] and platform.rect.left > 0:
            platform.rect.left -= platform.speed
        if key[pg.K_d] and platform.rect.right < screen_width:
            platform.rect.right += platform.speed
        if key[pg.K_ESCAPE]:
            exit()
        screen.blit(img, (0, 0))
        ball.update()
        for b in bonuses:
            b.update()
            if object_collision(platform, b):
                eval(b.bonus)
                bonus_balls.remove(b)
        if ball.is_out():
            EndGameScenario(win=False)
            game()
        ball.wall_bounce()
        object_collision(platform, ball)
        for block in blocks:
            object_collision(block, ball)
            block.update()
            if len(blocks) == 0:
                EndGameScenario(win=True)
                game()
        #draw_objects(platform, ball, blocks, bonuses)
        blocks.draw(screen)
        ball.draw()
        platform.draw()
        clock.tick(fps)


if __name__ == '__main__':
    game()
