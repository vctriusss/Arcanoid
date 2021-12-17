from constants import screen, screen_height, screen_width, pg


class Platform:
    """
    Platform is a moving object, which is controled by a keybord (control keys can be found in README.md file)
    Platform is needed to keep the ball inside the game area (ball bounces from it the as from the wall)
    Hitbox of the platform is a pygame.Rect() object
    """
    def __init__(self):
        """
        Initialisation of the platform
        It emerges in the bottom center of the screen
        """
        self.width = 150
        self.height = 10
        self.speed = 10
        self.body = pg.Rect(screen_width // 2 - self.width // 2, screen_height - self.height - 5,
                            self.width, self.height)
        self.color = pg.Color('magenta')

    def resize(self, k):
        """
        Function, that resizes the platform
        :param k: increment or decrement of the resize (new platform width will be k*width)
        :return: None
        """
        pg.draw.rect(screen, pg.Color('white'), self.body)
        self.body = self.body.inflate((k-1) * self.width, 0)

    def draw(self, col=None):
        """
        Function that draws the platform on the screen
        :param col: color of object, if not given, object will be drawn with default color
        :return: None
        """
        color = col if col else self.color
        pg.draw.rect(screen, color, self.body, border_radius=3)
