import unittest

from algs.easy.number_of_1_bits import Solution


class TestNumberOf1Bits(unittest.TestCase):
    def test_eleven_has_three_set_bits(self):
        self.assertEqual(Solution().hammingWeight(11), 3)

    def test_power_of_two_has_one_set_bit(self):
        self.assertEqual(Solution().hammingWeight(128), 1)

    def test_large_number_has_thirty_set_bits(self):
        self.assertEqual(Solution().hammingWeight(2147483645), 30)


if __name__ == "__main__":
    unittest.main()
