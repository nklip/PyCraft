# LeetCode 1768: Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/description/
# Task: Build a string by taking characters alternately from word1 and word2,
# beginning with word1. Once either word is exhausted, append the remaining
# characters of the other word in their original order.
class Solution:
    # Time Complexity: O((m + n)^2) worst case, from repeated string concatenation.
    # Space Complexity: O(m + n), for the result and temporary concatenation copies.
    # m = len(word1), n = len(word2); concatenation may copy the growing prefix.
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = len(word1) + len(word2)

        w1 = 0
        w2 = 0

        result = ''

        for i in range(length):

            if w1 == w2 and w1 < len(word1) or w2 == len(word2):
                result += word1[w1]
                w1 += 1
            else:
                result += word2[w2]
                w2 += 1
        return result
