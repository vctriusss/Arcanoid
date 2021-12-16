from constants import screen_width, screen_height, screen
import pygame as pg


class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.r = 8
        self.R = int(self.r * (2 ** 0.5))
        self.rect = pg.Rect(screen_width // 2 - self.r, screen_height - 15 - 2 * self.R, 2 * self.r, 2 * self.r)
        self.center = self.rect.x + self.r, self.rect.y + self.r
        self.dx = 1
        self.dy = -1
        self.speed = 6
        self.image = pg.Surface((self.r, self.r))

    # def fly(self):
    #     self.rect.x += self.dx * self.speed
    #     self.rect.y += self.dy * self.speed
    #     self.center = self.rect.x + self.r, self.rect.y + self.r
    def update(self, *args, **kwargs):
        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed
        self.center = self.rect.x + self.r, self.rect.y + self.r

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
