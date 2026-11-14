import unittest

from algs.easy.power_of_two import Solution


class TestPowerOfTwo(unittest.TestCase):
    def test_one_is_power_of_two(self):
        self.assertTrue(Solution().isPowerOfTwo(1))

    def test_sixteen_is_power_of_two(self):
        self.assertTrue(Solution().isPowerOfTwo(16))

    def test_three_is_not_power_of_two(self):
        self.assertFalse(Solution().isPowerOfTwo(3))


if __name__ == "__main__":
    unittest.main()
