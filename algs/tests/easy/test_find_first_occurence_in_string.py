import unittest

from algs.easy.find_first_occurence_in_string import Solution


class TestFindFirstOccurrenceInString(unittest.TestCase):
    def test_returns_first_occurrence(self):
        self.assertEqual(Solution().strStr("sadbutsad", "sad"), 0)

    def test_returns_minus_one_when_needle_is_absent(self):
        self.assertEqual(Solution().strStr("leetcode", "leeto"), -1)


if __name__ == "__main__":
    unittest.main()
