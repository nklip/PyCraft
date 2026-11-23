import unittest

from algs.easy.reverse_string import Solution


class TestReverseString(unittest.TestCase):
    def test_reverses_hello(self):
        s = ["h", "e", "l", "l", "o"]

        Solution().reverseString(s)

        self.assertEqual(s, ["o", "l", "l", "e", "h"])

    def test_reverses_hannah_preserving_case(self):
        s = ["H", "a", "n", "n", "a", "h"]

        Solution().reverseString(s)

        self.assertEqual(s, ["h", "a", "n", "n", "a", "H"])


if __name__ == "__main__":
    unittest.main()
