import pygame as pg
from constants import *
from Block import Block


class Bonus():
    def __init__(self, block: Block):
        self.center = block.body.center
        self.r = 6
        self.x = self.center[0] - self.r
        self.y = self.center[1] + self.r
        self.R = int(self.r * (2 ** 0.5))
        self.speed = 3
        self.body = pg.Rect(self.x, self.y, 2 * self.r, 2 * self.r)
        self.bonus = block.bonus
        self.dy = 1
        self.dx = 0
        self.color = [pg.Color('green'), pg.Color('red')][bonuses.index(self.bonus) % 2]
        self.image = pg.Surface((self.r, self.r))

    def draw(self):
        pg.draw.circle(screen, self.color, self.center, self.R)

    def fly(self):
        self.body.y += self.dy * self.speed
        self.center = self.body.x + self.r, self.body.y + self.r
