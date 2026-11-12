import unittest

from algs.easy.merge_strings_alternately import Solution


class TestMergeStringsAlternately(unittest.TestCase):
    def test_equal_length_words(self):
        self.assertEqual(Solution().mergeAlternately("abc", "pqr"), "apbqcr")

    def test_second_word_is_longer(self):
        self.assertEqual(Solution().mergeAlternately("ab", "pqrs"), "apbqrs")

    def test_first_word_is_longer(self):
        self.assertEqual(Solution().mergeAlternately("abcd", "pq"), "apbqcd")


if __name__ == "__main__":
    unittest.main()
