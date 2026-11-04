import unittest

from algs.easy.contains_duplicate import Solution


class TestContainsDuplicate(unittest.TestCase):
    def test_duplicate_numbers(self):
        self.assertTrue(Solution().containsDuplicate([1, 2, 3, 1]))

    def test_all_numbers_are_unique(self):
        self.assertFalse(Solution().containsDuplicate([1, 2, 3, 4]))

    def test_multiple_duplicate_numbers(self):
        self.assertTrue(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    def test_empty_list(self):
        self.assertFalse(Solution().containsDuplicate([]))

    def test_single_number(self):
        self.assertFalse(Solution().containsDuplicate([1]))

    def test_duplicate_negative_numbers(self):
        self.assertTrue(Solution().containsDuplicate([-1, 2, -1]))

    def test_duplicate_zeros(self):
        self.assertTrue(Solution().containsDuplicate([0, 0]))


if __name__ == "__main__":
    unittest.main()
