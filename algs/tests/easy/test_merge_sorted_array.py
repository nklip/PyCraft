import unittest

from algs.easy.merge_sorted_array import Solution


class TestMergeSortedArray(unittest.TestCase):
    def test_merges_two_nonempty_arrays(self):
        nums1 = [1, 2, 3, 0, 0, 0]

        Solution().merge(nums1, 3, [2, 5, 6], 3)

        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_empty_second_array(self):
        nums1 = [1]

        Solution().merge(nums1, 1, [], 0)

        self.assertEqual(nums1, [1])

    def test_first_array_has_no_initial_elements(self):
        nums1 = [0]

        Solution().merge(nums1, 0, [1], 1)

        self.assertEqual(nums1, [1])


if __name__ == "__main__":
    unittest.main()
