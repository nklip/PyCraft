import unittest

from algs.easy.two_sum import Solution

class TestTwoSum(unittest.TestCase):
    def test_first_two_numbers(self):
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_last_two_numbers(self):
        self.assertEqual(Solution().twoSum([3, 2, 4], 6), [1, 2])

    def test_duplicate_numbers(self):
        self.assertEqual(Solution().twoSum([3, 3], 6), [0, 1])

if __name__ == "__main__":
    unittest.main()
