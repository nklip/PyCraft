import unittest

from algs.easy.palindrome_number import Solution


class TestPalindromeNumber(unittest.TestCase):
    def test_positive_palindrome(self):
        self.assertTrue(Solution().isPalindrome(121))

    def test_negative_number_is_not_palindrome(self):
        self.assertFalse(Solution().isPalindrome(-121))

    def test_ten_is_not_palindrome(self):
        self.assertFalse(Solution().isPalindrome(10))


if __name__ == "__main__":
    unittest.main()
