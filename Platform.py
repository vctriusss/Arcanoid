from constants import *


class Platform:
    def __init__(self):
        self.width = 150
        self.height = 10
        self.speed = 10
        self.body = pg.Rect(screen_width // 2 - self.width // 2, screen_height - self.height - 5,
                            self.width, self.height)

    def resize(self):
        pg.draw.rect(screen, pg.Color('white'), self.body)
        self.body = self.body.inflate(15, 0)

    def collision(self, ball):
        if self.body.colliderect(ball.body):
            ball.dy = -1
            pg.draw.rect(screen, pg.Color('white'), self.body)

    def draw(self):
        pg.draw.rect(screen, pg.Color('magenta'), self.body, border_radius=3)
