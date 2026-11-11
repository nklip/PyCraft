# LeetCode 58: Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/
# Task: Return the number of characters in the final word of s, ignoring any
# trailing spaces. Words are runs of non-space characters separated by spaces.
class Solution:
    # Time Complexity: O(n) worst case, scanning trailing spaces and the last word.
    # Space Complexity: O(1), using only an index and a length counter.
    # n = len(s).
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        length = 0
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
