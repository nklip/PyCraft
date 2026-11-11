# LeetCode 14: Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/
# Task: Return the longest starting sequence of characters shared by every
# string in strs. Return an empty string when there is no shared prefix.
class Solution:
    # Time Complexity: O(n * m) worst case, comparing columns across the strings.
    # Space Complexity: O(p) for the returned prefix slice; O(1) auxiliary space.
    # n = len(strs), m = length of the first string, p = returned prefix length.
    # An empty list or an empty first string returns in O(1) time and space.
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""

        first_word = strs[0]

        end = 0

        terminate = False
        for i in range(len(first_word)):
            ch = first_word[i]

            for y in range(1, len(strs)):

                word = strs[y]

                if i >= len(word) or ch != word[i]:
                    terminate = True
                    break

            if terminate:
                break

            end += 1

        return first_word[0:end]
