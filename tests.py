import unittest
from main import Ball, ObjectCollision, Platform, Bonus, AssignBonuses
from Block import Block
from constants import screen_width, screen_height, bonuses
from block_patterns import choice, patterns


class GameTest(unittest.TestCase):
    def test_out_of_bounds(self):
        ball = Ball(150, 730)
        self.assertTrue(ball.IsOut())

    def test_in_bounds(self):
        ball = Ball(0, 0)
        self.assertFalse(ball.IsOut())

    def test_right_collision(self):
        ball = Ball(100, 100)
        block = Block(50, 50, 60, 60, (0, 0, 0))
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

    def test_hit_left(self):
        ball = Ball(35, 55)
        ball.dx = 1
        block = Block(50, 50, 60, 60, (0, 0, 0))
        ObjectCollision(block, ball)
        self.assertEqual(ball.dx, -1)

    def test_hit_right(self):
        ball = Ball(105, 55)
        ball.dx = -1
        block = Block(50, 50, 60, 60, (0, 0, 0))
        ObjectCollision(block, ball)
        self.assertEqual(ball.dx, 1)

    def test_hit_top(self):
        ball = Ball(105, 35)
        ball.dy = 1
        block = Block(50, 50, 60, 60, (0, 0, 0))
        ObjectCollision(block, ball)
        self.assertEqual(ball.dy, -1)

    def test_hit_bottom(self):
        ball = Ball(105, 105)
        ball.dy = -1
        block = Block(50, 50, 60, 60, (0, 0, 0))
        ObjectCollision(block, ball)
        self.assertEqual(ball.dy, 1)

    def test_hit_corner(self):
        ball = Ball(45, 46)
        ball.dx, ball.dy = 1, 1
        block = Block(50, 50, 60, 60, (0, 0, 0))
        ObjectCollision(block, ball)
        self.assertEqual((ball.dx, ball.dy), (-1, -1))

    def test_bonus_apply(self):
        block = Block(600, 1, 1, 1, (0, 0, 0))
        block.bonus = bonuses[0]
        bonus = Bonus(block)
        platform = Platform()
        bonus.body.bottom = platform.body.top + 1
        if ObjectCollision(platform, bonus):
            exec(bonus.bonus)
        self.assertEqual(platform.body.width, 187)

    def test_fly(self):
        ball = Ball(10, 10)
        ball.dx = 1
        x0, y0 = ball.center
        ball.fly()
        self.assertEqual(ball.center, (x0 + 6, y0 - 6))

    def test_probability(self):
        pattern = AssignBonuses(choice(patterns))
        bonus_list = [b.bonus is not None for b in pattern]
        self.assertTrue(sum(bonus_list) <= 0.2 * len(pattern))


if __name__ == '__main__':
    unittest.main()
