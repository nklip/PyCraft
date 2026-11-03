import unittest

from algs.easy.backspace_string_compare import Solution


class TestBackspaceStringCompare(unittest.TestCase):
    def test_both_strings_become_ac(self):
        self.assertTrue(Solution().backspaceCompare("ab#c", "ad#c"))

    def test_both_strings_become_empty(self):
        self.assertTrue(Solution().backspaceCompare("ab##", "c#d#"))

    def test_strings_differ_after_backspace(self):
        self.assertFalse(Solution().backspaceCompare("a#c", "b"))


if __name__ == "__main__":
    unittest.main()
