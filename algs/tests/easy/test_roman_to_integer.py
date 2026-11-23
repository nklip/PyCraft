import unittest

from algs.easy.roman_to_integer import Solution


class TestRomanToInteger(unittest.TestCase):
    def test_three(self):
        self.assertEqual(Solution().romanToInt("III"), 3)

    def test_fifty_eight(self):
        self.assertEqual(Solution().romanToInt("LVIII"), 58)

    def test_subtractive_pairs(self):
        self.assertEqual(Solution().romanToInt("MCMXCIV"), 1994)


if __name__ == "__main__":
    unittest.main()
