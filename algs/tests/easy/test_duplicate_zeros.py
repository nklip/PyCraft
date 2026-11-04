import unittest

from algs.easy.duplicate_zeros import Solution


class TestDuplicateZeros(unittest.TestCase):
    def test_duplicates_zeros_in_place(self):
        arr = [1, 0, 2, 3, 0, 4, 5, 0]

        Solution().duplicateZeros(arr)

        self.assertEqual(arr, [1, 0, 0, 2, 3, 0, 0, 4])

    def test_array_without_zeros_is_unchanged(self):
        arr = [1, 2, 3]

        Solution().duplicateZeros(arr)

        self.assertEqual(arr, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
