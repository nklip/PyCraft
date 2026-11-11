import unittest

from algs.majority_element import Solution


class TestMajorityElement(unittest.TestCase):
    def test_three_is_majority(self):
        self.assertEqual(Solution().majorityElement([3, 2, 3]), 3)

    def test_two_is_majority(self):
        self.assertEqual(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
