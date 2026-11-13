import unittest

from algs.easy.minimum_difference_between_highest_and_lowest_of_k_scores import (
    Solution,
)


class TestMinimumDifferenceBetweenHighestAndLowestOfKScores(unittest.TestCase):
    def test_single_score_has_zero_difference(self):
        self.assertEqual(Solution().minimumDifference([90], 1), 0)

    def test_smallest_difference_between_two_scores(self):
        self.assertEqual(Solution().minimumDifference([9, 4, 1, 7], 2), 2)


if __name__ == "__main__":
    unittest.main()
