import pygame as pg

res = screen_width, screen_height = 1200, 720
fps = 60


class Platform:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.speed = 10
        self.body = pg.Rect(screen_width // 2 - self.width // 2, screen_height - self.height - 5,
                            self.width, self.height)

    def resize(self):
        pg.draw.rect(screen, pg.Color('white'), platform.body)
        self.body = self.body.inflate(15, 0)


platform = Platform()

pg.init()
screen = pg.display.set_mode(res)
img = pg.image.load('image.jpg').convert()
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    screen.blit(img, (0, 0))
    pg.draw.rect(screen, pg.Color('magenta'), platform.body)
    key = pg.key.get_pressed()
    if key[pg.K_a] and platform.body.left > 0:
        platform.body.left -= platform.speed

    if key[pg.K_d] and platform.body.right < screen_width:
        platform.body.right += platform.speed

    pg.display.flip()
    clock.tick(fps)
