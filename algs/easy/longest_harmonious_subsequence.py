# LeetCode 594: Longest Harmonious Subsequence
# https://leetcode.com/problems/longest-harmonious-subsequence/description/
# Task: Find the greatest length of a subsequence whose largest and smallest
# values differ by exactly one. Chosen elements need not be adjacent. Return 0
# if no such subsequence exists; equal values alone do not qualify.
class Solution:
    # Time Complexity: O(n) average, counting values and checking adjacent keys.
    # Space Complexity: O(d), for the frequency dictionary of distinct values.
    # n = len(nums), d = number of distinct values; d <= n.
    # Dictionary operations take O(1) on average.
    def findLHS(self, nums: list[int]) -> int:
        dict = {}

        for key in nums:
            count = dict.get(key, 0)

            count += 1

            dict[key] = count

        max_length = 0

        for key, value in dict.items():
            start_key = key
            end_key = key + 1

            if end_key in dict:
                length = value + dict.get(end_key)

                if length > max_length:
                    max_length = length
        return max_length
