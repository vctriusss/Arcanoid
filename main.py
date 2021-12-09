import pygame as pg

screen_width, screen_height = 1200, 800
fps = 60


class Platform:
    def __init__(self):
        self.length = 300
        self.height = 30
        self.speed = 10

    def resize(self, c):
        self.length *= c


platform = Platform()
pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()


    pg.display.flip()
    clock.tick(fps)