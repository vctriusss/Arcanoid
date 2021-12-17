import unittest
from main import Ball, ObjectCollision
from Block import Block
import pygame as pg


class GameTest(unittest.TestCase):
    def test_out_of_bounds(self):
        ball = Ball(150, 730)
        self.assertTrue(ball.IsOut())

    def test_in_bounds(self):
        ball = Ball(0, 0)
        self.assertFalse(ball.IsOut())

    def right_collision(self):
        ball = Ball(100, 100)
        block = Block(50, 50, 60, 60, pg.Color('white'))
        self.assertTrue(ObjectCollision(block, ball))


if __name__ == '__main__':
    unittest.main()
