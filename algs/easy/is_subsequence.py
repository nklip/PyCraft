# LeetCode 392: Is Subsequence
# https://leetcode.com/problems/is-subsequence/description/
# Task: Check whether s can be obtained by deleting characters from input while
# keeping the remaining characters in their original order. Matching characters
# need not be adjacent, and an empty s is always a subsequence.
class Solution:
    # Time Complexity: O(n), scanning input once until all of s is matched.
    # Space Complexity: O(1), tracking only the next character to match.
    # n = len(input).
    def isSubsequence(self, s: str, input: str) -> bool:
        if s is None or len(s) == 0:
            return True

        if input is None or len(input) == 0:
            return False

        lf_index = 0

        for ch_at in input:
            ch_lf = s[lf_index]

            if ch_at == ch_lf:
                lf_index += 1
                if lf_index == len(s):
                    return True
        return False
