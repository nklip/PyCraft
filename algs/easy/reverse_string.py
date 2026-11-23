# LeetCode 344: Reverse String
# https://leetcode.com/problems/reverse-string/description/
# Task: Reverse the character list s in place using constant extra memory.
# Swap characters from opposite ends toward the middle; the method returns
# None, and the result is stored in the original list.
class Solution:
    # Time Complexity: O(n), swapping at most n // 2 pairs of characters.
    # Space Complexity: O(1), using two indices and one temporary character.
    # n = len(s).
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1
