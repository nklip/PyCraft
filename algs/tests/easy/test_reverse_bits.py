import unittest

from algs.easy.reverse_bits import Solution


class TestReverseBits(unittest.TestCase):
    def test_reverses_43261596(self):
        self.assertEqual(Solution().reverseBits(43261596), 964176192)

    def test_reverses_2147483644(self):
        self.assertEqual(Solution().reverseBits(2147483644), 1073741822)


if __name__ == "__main__":
    unittest.main()
