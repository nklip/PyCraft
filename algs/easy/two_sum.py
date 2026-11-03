# LeetCode 1: Two Sum
# https://leetcode.com/problems/two-sum/description/
# Task: Find two distinct indices in nums whose values sum to target.
# Exactly one valid pair is guaranteed; either index order is acceptable.
# Follow-up: Achieve a runtime better than O(n^2).
class Solution:

    # Time Complexity: O(n) on average, with constant-time dictionary operations.
    # Space Complexity: O(n), for the dictionary of previously seen values.
    # n = len(nums).
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # create dict
        seen = {}
        # normal for only gives you values
        for index, value in enumerate(nums):
            needed = target - value
            # if found - we got our pair of indexes
            if needed in seen:
                return [seen[needed], index]
            # not found - put value with the index in dict
            seen[value] = index
        return [0]
