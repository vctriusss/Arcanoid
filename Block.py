from constants import *


class Block:
    def __init__(self, x, y, w, h, color):
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.body = pg.Rect(self.x, self.y, self.width, self.height)
        self.color = color
