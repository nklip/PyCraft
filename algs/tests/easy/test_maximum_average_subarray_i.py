import unittest

from algs.easy.maximum_average_subarray_i import Solution


class TestMaximumAverageSubarrayI(unittest.TestCase):
    def test_maximum_average_of_four_elements(self):
        self.assertAlmostEqual(
            Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4), 12.75
        )

    def test_single_element(self):
        self.assertAlmostEqual(Solution().findMaxAverage([5], 1), 5.0)


if __name__ == "__main__":
    unittest.main()
