import pygame as pg

res = screen_width, screen_height = 1200, 800
fps = 60

# class Platform:
#     def __init__(self):
#         self.width = 300
#         self.height = 30
#         self.speed = 10
#         self.body = pg.Rect(screen_width // 2 - self.width // 2,
#                             screen_height - self.height, self.width, self.height)

platform_width, platform_height = 300, 30
platform_speed = 15
platform = pg.Rect(screen_width // 2 - platform_width // 2, screen_height - platform_height,
                   platform_width, platform_height)

pg.init()
screen = pg.display.set_mode(res)
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    pg.draw.rect(screen, pg.Color('blue'), platform)
    key = pg.key.get_pressed()
    if key[pg.K_a] and platform.left > 0:
        platform.left -= platform_speed

    if key[pg.K_d] and platform.right < screen_width:
        platform.right += platform_speed
    if key[pg.K_w]:
        screen.blit(img, (0, 0))
    pg.display.flip()
    clock.tick(fps)
