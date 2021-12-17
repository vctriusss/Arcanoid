from constants import bonuses, pg, screen, screen_height
from Block import Block


class Bonus:
    """
    Bonus is similar to a ball
    Ball on the screen is displayed as a circle of radius R
    Ball has a parameter body, which is basically a hitbox of a ball
    Body itself is a pygame.Rect() object, geometrically it is a square, which is inscried in a circle with radius R
    """
    def __init__(self, block: Block):
        """
        Initialisation of a bonus
        :param block: block, from which bonus ball comes
        """
        self.center = block.body.center  # centers of block and its bonus ball are the same
        self.r = 7
        self.x = self.center[0] - self.r
        self.y = self.center[1] + self.r
        self.R = int(self.r * (2 ** 0.5))
        self.speed = 3
        self.body = pg.Rect(self.x, self.y, 2 * self.r, 2 * self.r)
        self.bonus = block.bonus  # block parameter bonus (effect of a bonus) is transfered to a ball bonus
        self.dy = 1
        self.dx = 0
        self.color = [pg.Color('green'), pg.Color('red')][bonuses.index(self.bonus) % 2]
        self.image = pg.Surface((self.r, self.r))

    def draw(self):
        """
        Function that draws the bonus ball on the screen
        :return: None
        """
        pg.draw.circle(screen, self.color, self.center, self.R)

    def drop(self):
        """
        Basic function of bonus ball movement on the screen
        Updates the ball coordinates using its speed
        :return: None
        """
        self.body.y += self.dy * self.speed
        self.center = self.body.x + self.r, self.body.y + self.r

    def is_out(self):
        """
        Function checks whether the bonus is out out screen (top y coordinate > screen height)
        :return: True if ball is out of bounds, else False
        """
        return self.center[1] - self.R > screen_height
