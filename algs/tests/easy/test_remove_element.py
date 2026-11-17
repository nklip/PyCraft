import unittest

from algs.easy.remove_element import Solution


class TestRemoveElement(unittest.TestCase):
    def test_removes_threes(self):
        nums = [3, 2, 2, 3]

        k = Solution().removeElement(nums, 3)

        self.assertEqual(k, 2)
        self.assertCountEqual(nums[:k], [2, 2])

    def test_removes_twos_preserving_other_values(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]

        k = Solution().removeElement(nums, 2)

        self.assertEqual(k, 5)
        self.assertCountEqual(nums[:k], [0, 1, 3, 0, 4])


if __name__ == "__main__":
    unittest.main()
