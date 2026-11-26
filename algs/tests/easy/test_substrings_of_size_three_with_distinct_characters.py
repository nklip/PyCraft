import unittest

from algs.easy.substrings_of_size_three_with_distinct_characters import Solution


class TestSubstringsOfSizeThreeWithDistinctCharacters(unittest.TestCase):
    def test_one_good_substring(self):
        self.assertEqual(Solution().countGoodSubstrings("xyzzaz"), 1)

    def test_four_good_substrings(self):
        self.assertEqual(Solution().countGoodSubstrings("aababcabc"), 4)


if __name__ == "__main__":
    unittest.main()
