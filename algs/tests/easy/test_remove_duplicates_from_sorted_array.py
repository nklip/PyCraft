import unittest

from algs.easy.remove_duplicates_from_sorted_array import Solution


class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    def test_removes_one_duplicate(self):
        nums = [1, 1, 2]

        k = Solution().removeDuplicates(nums)

        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])

    def test_removes_multiple_duplicates(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

        k = Solution().removeDuplicates(nums)

        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0, 1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
