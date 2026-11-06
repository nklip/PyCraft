import unittest

from algs.easy.happy_number import Solution


class TestHappyNumber(unittest.TestCase):
    def test_nineteen_is_happy(self):
        self.assertTrue(Solution().isHappy(19))

    def test_two_is_not_happy(self):
        self.assertFalse(Solution().isHappy(2))


if __name__ == "__main__":
    unittest.main()
