import time
from constants import *
from Platform import Platform
from Ball import Ball
from block_patterns import patterns, choice
from Bonus import Bonus

pg.init()
pg.display.set_caption('Arcanoid')
img = pg.image.load('backgroundd.jpg')


def EndGameScenario(win: bool):
    """
    Function displays scenario when has ended
    Function waits for restart key(R) or exit key(ESC) to be pressed
    During this time it displays particular text according to win parameter
    :param win: True if player won (no blocks are left), False if player lost (ball is out of bounds)
    :return: True if restart key is pressed
    """
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
    """
    Basic function of game physics
    If collision is detected, it changes the fly direction of obj2 depending on a border, where static object was hit
    :param obj1: 'static' object (which doesn't fly), it can be platform or a block
    :param obj2: obj2 is a flying object (ball or bonus)
    :return: True if there is a collision, else False
    """
    if obj1.body.colliderect(obj2.body):
        delta_x = obj2.body.right - obj1.body.left if obj2.dx > 0 else obj1.body.right - obj2.body.left
        delta_y = obj2.body.bottom - obj1.body.top if obj2.dy > 0 else obj1.body.bottom - obj2.body.top
        # corner hit
        if abs(delta_x - delta_y) < 3:
            obj2.dx *= -1
            obj2.dy *= -1
        # left or right side hit
        elif delta_x > delta_y:
            obj2.dy *= -1
        # top or bottom side hit
        else:
            obj2.dx *= -1
        return True
    return False


def draw_objects(*args):
    """
    Function draws objects, which are given in args
    :param args: objects to be drawn (can be class object or a list of objects)
    :return: None
    """
    for arg in args:
        if type(arg) != list:
            arg.draw()
        else:
            for obj in arg:
                obj.draw()
    pg.display.flip()


def assign_bonuses(pattern: list):
    """
    Function assignes bonuses to 20% blocks in patterns, other block remain block.bonus = None as default
    :param pattern: pattern (list of all blocks)
    :return: None
    """
    size = len(pattern)
    n = int(0.2 * size)
    for i in range(n):
        b = choice(pattern)
        b.bonus = choice(bonuses)


def game(pattern: list):
    """
    Main function of the game
    :param pattern: pattern of blocks for this session of game
    :return: None
    """
    bonus_balls.clear()
    platform = Platform()
    ball = Ball()
    block_pattern = pattern.copy()
    assign_bonuses(block_pattern)
    clock = pg.time.Clock()

    time_end = time.time() + 1
    while time.time() < time_end:
        screen.blit(img, (0, 0))
        draw_objects(platform, block_pattern)
        pg.display.flip()

    while True:
        # controls
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
        if ball.is_out():  # -> game over
            restart = EndGameScenario(win=False)
            if restart:
                game(choice(patterns))
        ball.wall_bounce()
        if object_collision(platform, ball):
            platform.draw(col=pg.Color('white'))

        for block in block_pattern:
            if object_collision(block, ball):
                block.draw(col=pg.Color('white'))
                block_pattern.remove(block)
                if block.bonus:
                    bonus_balls.append(Bonus(block))

        if len(block_pattern) == 0:  # no blocks are left -> game won
            screen.blit(img, (0, 0))
            EndGameScenario(win=True)
            game(choice(patterns))

        for bb in bonus_balls:
            bb.drop()
            if bb.is_out():
                bonus_balls.remove(bb)
            if bb.body.colliderect(platform.body):
                exec(bb.bonus)  # applying a bonus
                bonus_balls.remove(bb)

        draw_objects(platform, ball, block_pattern, bonus_balls)
        clock.tick(fps)


if __name__ == '__main__':
    game(choice(patterns))
