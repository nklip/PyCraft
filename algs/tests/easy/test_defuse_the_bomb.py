import unittest

from algs.easy.defuse_the_bomb import Solution


class TestDefuseTheBomb(unittest.TestCase):
    def test_positive_k_sums_next_numbers_with_wraparound(self):
        self.assertEqual(Solution().decrypt([5, 7, 1, 4], 3), [12, 10, 16, 13])

    def test_zero_k_returns_zeros(self):
        self.assertEqual(Solution().decrypt([1, 2, 3, 4], 0), [0, 0, 0, 0])

    def test_negative_k_sums_previous_numbers_with_wraparound(self):
        self.assertEqual(Solution().decrypt([2, 4, 9, 3], -2), [12, 5, 6, 13])


if __name__ == "__main__":
    unittest.main()
