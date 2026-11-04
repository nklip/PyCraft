# LeetCode 217: Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/
# Task: Return whether any integer occurs more than once in nums.
# Return False when all values are distinct.
class Solution:
    # Time Complexity: O(n log n), sorting nums before scanning adjacent values.
    # Space Complexity: O(n) worst case, for Python's sorting workspace.
    # n = len(nums); sorting modifies the input list.
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()

        for i in range (1, len(nums)):
            prev = nums[i - 1]
            curr = nums[i]

            if prev == curr:
                return True
        return False
