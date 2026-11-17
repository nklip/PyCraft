# LeetCode 26: Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# Task: Compact a nonempty, sorted nums in place, keeping each distinct value
# once in sorted order at the front. Return the count k of retained values;
# only nums[:k] matters, and entries beyond that prefix may be ignored.
class Solution:
    # Time Complexity: O(n), scanning once and writing each new distinct value.
    # Space Complexity: O(1), using read and write indices without another list.
    # n = len(nums); the input list is modified but not resized.
    def removeDuplicates(self, nums: list[int]) -> int:
        id_unique_pos = 1

        for i in range(1, len(nums)):
            value = nums[i]

            unique_value = nums[id_unique_pos - 1]

            if unique_value != value:
                nums[id_unique_pos] = value
                id_unique_pos += 1
        return id_unique_pos
