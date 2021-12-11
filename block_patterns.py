from Block import Block
from random import choice
from constants import colors


blocks1 = [Block(10 + 120 * i, 10 + 70 * j, 100, 30, choice(colors)) for i in range(10) for j in range(4)]
patterns = [blocks1, blocks1]
