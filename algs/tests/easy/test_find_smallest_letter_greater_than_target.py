import unittest

from algs.easy.find_smallest_letter_greater_than_target import Solution


class TestFindSmallestLetterGreaterThanTarget(unittest.TestCase):
    def test_target_before_first_letter(self):
        self.assertEqual(Solution().nextGreatestLetter(["c", "f", "j"], "a"), "c")

    def test_target_equal_to_letter_returns_next_greater_letter(self):
        self.assertEqual(Solution().nextGreatestLetter(["c", "f", "j"], "c"), "f")

    def test_target_after_last_letter_wraps_to_first_letter(self):
        self.assertEqual(
            Solution().nextGreatestLetter(["x", "x", "y", "y"], "z"), "x"
        )


if __name__ == "__main__":
    unittest.main()
