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


class Ball:
    def __init__(self):
        self.r = 10
        self.R = int(self.r * (2 ** 0.2))
        self.body = pg.Rect(screen_width // 2 - self.r, screen_height - 10 - int(0.4 * self.r), 2 * self.r, 2 * self.r)
        self.center = self.body.x + self.r, self.body.y - self.r
        self.dx = 1
        self.dy = -1
        self.speed = 5

    def fly(self):
        self.body.x += self.dx * self.speed
        self.body.y += self.dy * self.speed
        self.center = self.body.x + self.r, self.body.y - self.r

    def check_out(self):
        if self.center[1] - self.R > screen_height:
            black = pg.Rect(screen_width // 2 - 260, screen_height // 2 - 50, 500, 100)
            pg.draw.rect(screen, pg.Color('black'), black)
            screen.blit(text, (black.x + 10, black.y + 5))

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


platform = Platform()
ball = Ball()
pg.init()
pg.font.init()
textfont = pg.font.SysFont('Times New Roman', 80)
text = textfont.render('GAME OVER', True, pg.Color('red'))
screen = pg.display.set_mode(res)
img = pg.image.load('image.jpg').convert()
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    screen.blit(img, (0, 0))
    pg.draw.rect(screen, pg.Color('magenta'), platform.body)
    pg.draw.circle(screen, pg.Color('white'), ball.center, ball.R)
    ball.fly()
    ball.wall_bounce()
    ball.check_out()
    key = pg.key.get_pressed()
    if key[pg.K_a] and platform.body.left > 0:
        platform.body.left -= platform.speed

    if key[pg.K_d] and platform.body.right < screen_width:
        platform.body.right += platform.speed

    pg.display.flip()
    clock.tick(fps)
