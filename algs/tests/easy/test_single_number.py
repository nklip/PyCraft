import unittest

from algs.easy.single_number import Solution


class TestSingleNumber(unittest.TestCase):
    def test_single_number_after_pair(self):
        self.assertEqual(Solution().singleNumber([2, 2, 1]), 1)

    def test_single_number_with_separated_pairs(self):
        self.assertEqual(Solution().singleNumber([4, 1, 2, 1, 2]), 4)

    def test_single_element(self):
        self.assertEqual(Solution().singleNumber([1]), 1)


if __name__ == "__main__":
    unittest.main()
