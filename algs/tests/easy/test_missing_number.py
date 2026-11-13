import unittest

from algs.easy.missing_number import Solution


class TestMissingNumber(unittest.TestCase):
    def test_missing_two_from_unsorted_numbers(self):
        self.assertEqual(Solution().missingNumber([3, 0, 1]), 2)

    def test_missing_upper_bound(self):
        self.assertEqual(Solution().missingNumber([0, 1]), 2)

    def test_missing_eight(self):
        self.assertEqual(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)


if __name__ == "__main__":
    unittest.main()
