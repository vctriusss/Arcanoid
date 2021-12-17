from Block import Block
from random import choice
from constants import colors


blocks1 = [Block(10 + 120 * i, 10 + 70 * j, 100, 30, choice(colors)) for i in range(10) for j in range(4)]
blocks_test = [Block(1100, 120, 100, 30, choice(colors)),
               Block(500, 120, 100, 30, choice(colors))]
patterns = [blocks_test]
