# LeetCode 1876: Substrings of Size Three with Distinct Characters
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/
# Task: Count contiguous substrings of length three whose characters are all
# different. Count each occurrence separately, including overlapping windows
# and repeated occurrences of the same three-character substring.
class Solution:
    # Time Complexity: O(n), making at most three comparisons per window.
    # Space Complexity: O(1), using an index and counter without creating slices.
    # n = len(s); strings shorter than three characters have no such windows.
    def countGoodSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s) - 2):
            if s[i] != s[i+1] and s[i] != s[i+2] and s[i + 1] != s[i + 2]:
                count += 1
        return count
