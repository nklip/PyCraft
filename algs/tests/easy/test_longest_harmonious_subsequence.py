import unittest

from algs.easy.longest_harmonious_subsequence import Solution


class TestLongestHarmoniousSubsequence(unittest.TestCase):
    def test_repeated_adjacent_values(self):
        self.assertEqual(Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7]), 5)

    def test_consecutive_values(self):
        self.assertEqual(Solution().findLHS([1, 2, 3, 4]), 2)

    def test_identical_values_have_no_harmonious_subsequence(self):
        self.assertEqual(Solution().findLHS([1, 1, 1, 1]), 0)


if __name__ == "__main__":
    unittest.main()
