import unittest

from algs.easy.sqrt import Solution


class TestSqrt(unittest.TestCase):
    def test_perfect_square(self):
        self.assertEqual(Solution().mySqrt(4), 2)

    def test_non_perfect_square_rounds_down(self):
        self.assertEqual(Solution().mySqrt(8), 2)


if __name__ == "__main__":
    unittest.main()
