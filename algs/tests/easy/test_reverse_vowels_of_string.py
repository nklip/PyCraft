import unittest

from algs.easy.reverse_vowels_of_string import Solution


class TestReverseVowelsOfString(unittest.TestCase):
    def test_reverses_mixed_case_vowels(self):
        self.assertEqual(Solution().reverseVowels("IceCreAm"), "AceCreIm")

    def test_reverses_lowercase_vowels(self):
        self.assertEqual(Solution().reverseVowels("leetcode"), "leotcede")


if __name__ == "__main__":
    unittest.main()
