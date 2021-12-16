import pygame as pg

res = screen_width, screen_height = 1200, 720
fps = 60
screen = pg.display.set_mode(res)

pg.font.init()
textfont = pg.font.SysFont('Times New Roman', 80)
textfont_small = pg.font.SysFont('Times New Roman', 40)
text_gameover = textfont.render('GAME OVER', True, pg.Color('red'))
text_youwin = textfont.render('YOU WIN!', True, pg.Color('green'))
text_reload = textfont_small.render('Press R to restart', True, pg.Color('white'))

colors = ['magenta', 'yellow', 'cyan', 'blue2', 'green', 'darkmagenta', 'deeppink']
bonuses = ['platform.resize(1.25)', 'platform.resize(0.75)', 'ball.speed *= 1.25', 'ball.speed *= 0.75']
bonus_balls = []
