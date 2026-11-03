# LeetCode 844: Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/description/
# Task: Compare the text produced by s and t after applying '#' as backspace.
# A backspace with nothing left to delete has no effect. Return whether the
# two resulting texts match.
# Follow-up: Use O(n + m) time and O(1) auxiliary space.
class Solution:
    # Time Complexity: O(n^2 + m^2) worst case, from repeated string concatenation.
    # Space Complexity: O(n + m), for the two constructed strings.
    # n = len(s), m = len(t); string concatenation may copy the growing prefix.
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = self.replaceBackspace(s)
        s2 = self.replaceBackspace(t)

        return s1 == s2

    def replaceBackspace(self, s: str):
        sb = ''
        right = len(s) - 1
        count_back = 0

        while right >= 0:
            right_ch = s[right]

            if right_ch is '#':
                count_back += 1
            elif count_back > 0:
                count_back -= 1
            else:
                sb += s[right]
            right -= 1

        return sb
