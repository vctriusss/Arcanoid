import unittest
from main import Ball, ObjectCollision, Platform, Bonus
from Block import Block
from constants import *


class GameTest(unittest.TestCase):
    def test_out_of_bounds(self):
        ball = Ball(150, 730)
        self.assertTrue(ball.IsOut())

    def test_in_bounds(self):
        ball = Ball(0, 0)
        self.assertFalse(ball.IsOut())

    def test_right_collision(self):
        ball = Ball(100, 100)
        block = Block(50, 50, 60, 60, pg.Color('white'))
        self.assertTrue(ObjectCollision(block, ball))

    def test_correct_new_direction(self):
        ball = Ball(600, screen_height - 17)
        ball.dy = 1
        platform = Platform()
        ObjectCollision(platform, ball)
        self.assertEqual(ball.dy, -1)

    def test_wall_bounce(self):
        ball = Ball(screen_width - 16, 100)
        ball.dx = 1
        ball.WallBounce()
        self.assertEqual(ball.dx, -1)

    def test_bonus_apply(self):
        block = Block(600, 1, 1, 1, (0, 0, 0))
        block.bonus = bonuses[0]
        bonus = Bonus(block)
        platform = Platform()
        bonus.body.bottom = platform.body.top + 1
        if ObjectCollision(platform, bonus):
            exec(bonus.bonus)
        self.assertEqual(platform.body.width, 187)


if __name__ == '__main__':
    unittest.main()
