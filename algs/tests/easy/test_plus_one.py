import unittest

from algs.easy.plus_one import Solution


class TestPlusOne(unittest.TestCase):
    def test_increments_three_digit_number(self):
        self.assertEqual(Solution().plusOne([1, 2, 3]), [1, 2, 4])

    def test_increments_four_digit_number(self):
        self.assertEqual(Solution().plusOne([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_carry_creates_new_digit(self):
        self.assertEqual(Solution().plusOne([9]), [1, 0])


if __name__ == "__main__":
    unittest.main()
