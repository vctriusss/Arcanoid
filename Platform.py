from constants import *


class Platform(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.width = 150
        self.height = 10
        self.speed = 10
        self.rect = pg.Rect(screen_width // 2 - self.width // 2, screen_height - self.height - 5,
                            self.width, self.height)
        self.image = pg.Surface((self.width, self.height))

    def resize(self, k):
        pg.draw.rect(screen, pg.Color('white'), self.rect)
        self.rect = self.rect.inflate(int(self.width * (k-1)), 0)

    def draw(self):
        pg.draw.rect(screen, pg.Color('magenta'), self.rect, border_radius=3)
