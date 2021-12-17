from constants import screen_width, screen_height, screen
import pygame as pg
from random import randint, choice


class Ball:
    def __init__(self):
        self.r = 8
        self.R = int(self.r * (2 ** 0.5))
        self.body = pg.Rect(randint(0, screen_width // 2 - 100), screen_height, 2 * self.r, 2 * self.r)
        self.center = self.body.x + self.r, self.body.y + self.r
        self.dx = choice([-1, 1])
        self.dy = -1
        self.speed = 6

    def fly(self):
        self.body.x += self.dx * self.speed
        self.body.y += self.dy * self.speed
        self.center = self.body.x + self.r, self.body.y + self.r

    def is_out(self):
        return self.center[1] - self.R > screen_height

    def wall_bounce(self):
        # right wall
        if self.center[0] + self.R >= screen_width:
            self.dx = -self.dx
        # ceiling
        if self.center[1] - self.R <= 0:
            self.dy = -self.dy
        # left wall
        if self.center[0] - self.R <= 0:
            self.dx = -self.dx

    def draw(self):
        pg.draw.circle(screen, pg.Color('cyan'), self.center, self.R)
