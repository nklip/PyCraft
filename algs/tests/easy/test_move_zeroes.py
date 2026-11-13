import unittest

from algs.easy.move_zeroes import Solution


class TestMoveZeroes(unittest.TestCase):
    def test_moves_zeroes_to_end_preserving_nonzero_order(self):
        nums = [0, 1, 0, 3, 12]

        Solution().moveZeroes(nums)

        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_single_zero(self):
        nums = [0]

        Solution().moveZeroes(nums)

        self.assertEqual(nums, [0])


if __name__ == "__main__":
    unittest.main()
