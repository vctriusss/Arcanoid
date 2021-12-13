from constants import *
from Ball import Ball


class Block:
    def __init__(self, x, y, w, h, color):
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.body = pg.Rect(self.x, self.y, self.width, self.height)
        self.color = color
        self.bonus = None

    def draw(self):
        pg.draw.rect(screen, self.color, self.body, border_radius=3)

    def hit_by(self, ball: Ball):
        if self.body.colliderect(ball.body):
            # right and left border
            if ball.body.left == self.body.right or ball.body.right == self.body.left:
                ball.dx *= -1
            # bottom and topborder
            if ball.body.top == self.body.bottom or ball.body.bottom == self.body.top:
                ball.dy *= -1
            return True
        else:
            return False

