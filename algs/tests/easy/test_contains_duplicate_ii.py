import unittest

from algs.easy.contains_duplicate_ii import Solution


class TestContainsDuplicateII(unittest.TestCase):
    def test_duplicate_at_maximum_allowed_distance(self):
        self.assertTrue(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))

    def test_adjacent_duplicates(self):
        self.assertTrue(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))

    def test_duplicates_outside_allowed_distance(self):
        self.assertFalse(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))


if __name__ == "__main__":
    unittest.main()
