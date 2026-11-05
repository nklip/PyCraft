# LeetCode 28: Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# Task: Locate the earliest complete match of the nonempty needle in haystack.
# Return its zero-based starting index, or -1 when no match exists.
class Solution:
    # Time Complexity: O((n - m + 1) * m) worst case when n >= m, comparing
    # up to m characters at each candidate position; O(1) when n < m.
    # Space Complexity: O(1), comparing characters directly using indices.
    # n = len(haystack), m = len(needle).
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        index = -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                for y in range(1, len(needle)):
                    if len(haystack) < i + y + 1:
                        break
                    if haystack[i + y] != needle[y]:
                        break
                    if haystack[i + y] == needle[y] and y + 1 == len(needle):
                        index = i
                        break

                if index != -1:
                    break
                elif len(needle) == 1:
                    index = i
                    break
        return index
