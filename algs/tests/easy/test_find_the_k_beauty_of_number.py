import unittest

from algs.easy.find_the_k_beauty_of_number import Solution


class TestFindTheKBeautyOfNumber(unittest.TestCase):
    def test_both_substrings_are_divisors(self):
        self.assertEqual(Solution().divisorSubstrings(240, 2), 2)

    def test_zero_substring_and_repeated_divisors(self):
        self.assertEqual(Solution().divisorSubstrings(430043, 2), 2)


if __name__ == "__main__":
    unittest.main()
