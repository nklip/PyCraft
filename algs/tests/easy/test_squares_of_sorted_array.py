import unittest

from algs.easy.squares_of_sorted_array import Solution


class TestSquaresOfSortedArray(unittest.TestCase):
    def test_negative_positive_and_zero_values(self):
        self.assertEqual(
            Solution().sortedSquares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100]
        )

    def test_equal_squares_from_opposite_values(self):
        self.assertEqual(
            Solution().sortedSquares([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121]
        )


if __name__ == "__main__":
    unittest.main()
