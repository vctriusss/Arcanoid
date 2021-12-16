from constants import screen, pg


class Block(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, color, bonus):
        pg.sprite.Sprite.__init__(self)
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.color = color
        self.bonus = bonus
        self.image = pg.Surface((self.width, self.height))

    def draw(self):
        pg.draw.rect(screen, self.color, self.rect, border_radius=3)
