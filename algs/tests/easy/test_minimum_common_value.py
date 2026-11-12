import unittest

from algs.easy.minimum_common_value import Solution


class TestMinimumCommonValue(unittest.TestCase):
    def test_single_common_value(self):
        self.assertEqual(Solution().getCommon([1, 2, 3], [2, 4]), 2)

    def test_returns_smallest_of_multiple_common_values(self):
        self.assertEqual(Solution().getCommon([1, 2, 3, 6], [2, 3, 4, 5]), 2)


if __name__ == "__main__":
    unittest.main()
