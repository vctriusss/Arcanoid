import pygame as pg
import time

res = screen_width, screen_height = 1200, 720
fps = 60


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


class Ball:
    def __init__(self):
        self.r = 8
        self.R = int(self.r * (2 ** 0.5))
        self.body = pg.Rect(screen_width // 2 - self.r, screen_height - 15 - 2 * self.R, 2 * self.r, 2 * self.r)
        self.center = self.body.x + self.r, self.body.y + self.r
        self.dx = 1
        self.dy = -1
        self.speed = 5

    def fly(self):
        self.body.x += self.dx * self.speed
        self.body.y += self.dy * self.speed
        self.center = self.body.x + self.r, self.body.y + self.r

    def check_out(self):
        if self.center[1] - self.R > screen_height:
            black = pg.Rect(screen_width // 2 - 260, screen_height // 2 - 50, 500, 100)
            pg.draw.rect(screen, pg.Color('black'), black)
            screen.blit(text_gameover, (black.x + 10, black.y + 5))
            return True
        else:
            return False

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


pg.font.init()
textfont = pg.font.SysFont('Times New Roman', 80)
text_gameover = textfont.render('GAME OVER', True, pg.Color('red'))
text_youwin = textfont.render('YOU WIN!', True, pg.Color('green'))
img = pg.image.load('image.jpg')

pg.init()
screen = pg.display.set_mode(res)
def game():
    pg.init()
    screen = pg.display.set_mode(res)
    platform = Platform()
    ball = Ball()
    clock = pg.time.Clock()
    time_end = time.time() + 0.5
    while time.time() < time_end:
        screen.blit(img, (0, 0))
        pg.draw.rect(screen, pg.Color('magenta'), platform.body, border_radius=3)
        pg.draw.circle(screen, pg.Color('white'), ball.center, ball.R)
        pg.display.flip()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
        screen.blit(img, (0, 0))
        pg.draw.rect(screen, pg.Color('magenta'), platform.body, border_radius=3)
        pg.draw.circle(screen, pg.Color('white'), ball.center, ball.R)
        ball.fly()
        ball.wall_bounce()
        game_over = ball.check_out()
        platform.collision(ball)
        key = pg.key.get_pressed()
        if key[pg.K_a] and platform.body.left > 0:
            platform.body.left -= platform.speed

        if key[pg.K_d] and platform.body.right < screen_width:
            platform.body.right += platform.speed

        if key[pg.K_r] and game_over:
            game()
        pg.display.flip()
        clock.tick(fps)


game()