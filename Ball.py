from constants import screen_width, screen_height, screen
import pygame as pg
from random import choice


class Ball:
    """
    Ball on the screen is displayed as a circle of radius R
    Ball has a parameter body, which is basically a hitbox of a ball
    Body itself is a pygame.Rect() object, geometrically it is a square, which is inscried in a circle with radius R
    """
    def __init__(self, x, y):
        """
        Initialisation of Ball
        :param x: x coordinate of top left corner of the ball body
        :param y: y coordinate of top left corner of the ball body
        """
        self.r = 8
        self.R = int(self.r * (2 ** 0.5))
        self.body = pg.Rect(x, y, 2 * self.r, 2 * self.r)
        self.center = self.body.x + self.r, self.body.y + self.r
        # x direction is chosen randomly
        self.dx = choice([-1, 1])
        self.dy = -1
        self.speed = 6

    def fly(self):
        """
        Basic function of ball movement on the screen
        Updates the ball coordinates using its speed
        :return: None
        """
        self.body.x += self.dx * self.speed
        self.body.y += self.dy * self.speed
        self.center = self.body.x + self.r, self.body.y + self.r

    def IsOut(self):
        """
        Function checks whether the ball is out out screen (top y coordinate > screen height)
        :return: True if ball is out of bounds, else False
        """
        return self.center[1] - self.R > screen_height

    def WallBounce(self):
        """
        Basic function of ball bouncing from walls
        It changes ball direction according to a wall, which it has hit
        :return: None
        """
        # right wall
        if self.body.right >= screen_width:
            self.dx = -self.dx
        # ceiling
        if self.body.top <= 0:
            self.dy = -self.dy
        # left wall
        if self.body.left <= 0:
            self.dx = -self.dx

    def draw(self):
        """
        Function that draws the ball on the screen
        :return: None
        """
        pg.draw.circle(screen, pg.Color('cyan'), self.center, self.R)
