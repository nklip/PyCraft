import unittest

from algs.easy.climbing_stairs import Solution


class TestClimbingStairs(unittest.TestCase):
    def test_two_stairs_have_two_ways(self):
        self.assertEqual(Solution().climbStairs(2), 2)

    def test_three_stairs_have_three_ways(self):
        self.assertEqual(Solution().climbStairs(3), 3)


if __name__ == "__main__":
    unittest.main()
