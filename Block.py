from constants import screen, pg


class Block:
    """
    Block is a rectangle, which keeps a bonus in it
    Once the block is broken, a bonus ball emerges on its place with a bonus of this particular block
    Hitbox of the block is pygame.Rect() object
    """
    def __init__(self, x, y, w, h, color):
        """
        Initialisation of a block
        :param x: top left corner x coordinate of a block
        :param y: top left corner y coordinate of a block
        :param w: block width
        :param h: block height
        :param color: block color
        """
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.body = pg.Rect(self.x, self.y, self.width, self.height)
        self.color = color
        self.bonus = None

    def draw(self):
        """
        Function that draws the block on the screen
        :return: None
        """
        pg.draw.rect(screen, self.color, self.body, border_radius=3)
