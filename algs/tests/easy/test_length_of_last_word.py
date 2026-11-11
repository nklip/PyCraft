import unittest

from algs.easy.length_of_last_word import Solution


class TestLengthOfLastWord(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(Solution().lengthOfLastWord("Hello World"), 5)

    def test_leading_trailing_and_repeated_spaces(self):
        self.assertEqual(
            Solution().lengthOfLastWord("   fly me   to   the moon  "), 4
        )

    def test_luffy_is_still_joyboy(self):
        self.assertEqual(Solution().lengthOfLastWord("luffy is still joyboy"), 6)


if __name__ == "__main__":
    unittest.main()
