import unittest

from algs.easy.count_pairs_whose_sum_is_less_than_target import Solution


class TestCountPairsWhoseSumIsLessThanTarget(unittest.TestCase):
    def test_three_pairs_below_positive_target(self):
        self.assertEqual(Solution().countPairs([-1, 1, 2, 3, 1], 2), 3)

    def test_ten_pairs_below_negative_target(self):
        self.assertEqual(Solution().countPairs([-6, 2, 5, -2, -7, -1, 3], -2), 10)


if __name__ == "__main__":
    unittest.main()
