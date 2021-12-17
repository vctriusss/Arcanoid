import time
from constants import *
from Platform import Platform
from Ball import Ball
from block_patterns import patterns, choice
from Bonus import Bonus
from random import randint

pg.init()
pg.display.set_caption('Arcanoid')
img = pg.image.load('background.jpg')
img = pg.transform.scale(img, res)


def EndGameScenario(win: bool):
    """
    Function displays scenario when has ended
    Function waits for restart key(R) or exit key(ESC) to be pressed
    During this time it displays particular text according to win parameter
    :param win: True if player won (no blocks are left), False if player lost (ball is out of bounds)
    :return: True if restart key is pressed
    """
    black = pg.Rect(int(0.35 * screen_width), int(0.4 * screen_height), 500, 150)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    exit()
                elif event.key == pg.K_r:
                    return True
        # pg.draw.rect(screen, pg.Color('black'), black)
        if win:
            screen.blit(text_youwin, (black.x + 50, black.y + 5))
        else:
            screen.blit(text_gameover, (black.x + 10, black.y + 5))
        screen.blit(text_reload, (black.x + 20, black.y + 100))
        pg.display.flip()


# main idea of this function was borrowed and adopted from another project
# URL: https://github.com/StanislavPetrovV/Python-Arkanoid-Breakout
# start of borrowing
def ObjectCollision(obj1, obj2):
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
        if abs(delta_x - delta_y) < 5:
            obj2.dx *= -1
            obj2.dy *= -1
        # left or right side hit
        elif delta_x > delta_y:
            obj2.dy *= -1
        # top or bottom side hit
        elif delta_x < delta_y:
            obj2.dx *= -1
        return True
    return False
# end of borrowing


def DrawObjects(*args):
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
    balls.clear()
    # initialising all neccessary objects
    platform = Platform()
    # ball appears in a random spot on the bottom left side of the screen
    ball = Ball(randint(10, screen_width // 2 - 100), screen_height)
    balls.append(ball)
    block_pattern = pattern.copy()
    assign_bonuses(block_pattern)
    clock = pg.time.Clock()
    # small delay
    time_end = time.time() + 1
    while time.time() < time_end:
        screen.blit(img, (0, 0))
        DrawObjects(platform, block_pattern)
        pg.display.flip()
    # main loop
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
        # rendering ball movement
        for ball in balls:
            ball.fly()
            if ball.IsOut():
                balls.remove(ball)  # -> game over
                if len(balls) == 0:
                    restart = EndGameScenario(win=False)
                    if restart:
                        game(choice(patterns))  # new game
            if ObjectCollision(platform, ball) and ball.dy > 0:
                platform.draw(col=pg.Color('white'))  # hit flash
            ball.WallBounce()  # detecting wall collision

            # rendering block hit
            for block in block_pattern:
                if ObjectCollision(block, ball):
                    block.draw(col=pg.Color('white'))  # hit flash
                    block_pattern.remove(block)
                    if block.bonus:
                        bonus_balls.append(Bonus(block))  # initialising new bonus ball

        if len(block_pattern) == 0:  # no blocks are left -> game won
            screen.blit(img, (0, 0))
            EndGameScenario(win=True)
            game(choice(patterns))  # new game

        # rendering bonus balls movement
        for bb in bonus_balls:
            bb.drop()
            if bb.IsOut():
                bonus_balls.remove(bb)
            if bb.body.colliderect(platform.body):
                exec(bb.bonus)  # applying a bonus
                bonus_balls.remove(bb)

        DrawObjects(platform, balls, block_pattern, bonus_balls)
        clock.tick(fps)


if __name__ == '__main__':
    game(choice(patterns))
