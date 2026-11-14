# LeetCode 9: Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/
# Task: Check whether x has the same decimal representation in both directions.
# Negative numbers are not palindromes; zero is a palindrome.
class Solution:

    # half-reversal
    # Time Complexity: O(d) worst case, reversing roughly half of the digits.
    # Space Complexity: O(1), storing only the remaining and reversed portions.
    # d = number of decimal digits in abs(x), counting zero as one digit.
    # Assumes constant-time arithmetic for the problem's 32-bit input range.
    def isPalindrome(self, x: int) -> bool:
        # all negative numbers and multiples of 10 (except 0) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed = 0
        while x > reversed:
            reversed = reversed * 10 + (x % 10)
            x //= 10 # delete last digit
        # even-length: x == reversed, add-length: x == reversed / 10
        return x == reversed or x == reversed // 10
