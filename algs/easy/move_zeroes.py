# LeetCode 283: Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/
# Task: Rearrange nums so that every zero follows all nonzero values, preserving
# the original order of the nonzero values. Modify the list in place and return
# nothing.
class Solution:
    # Time Complexity: O(n), scanning once and swapping each nonzero value forward.
    # Space Complexity: O(1), using indices and temporary values without a copy.
    # n = len(nums).
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0

        for i in range (len(nums)):
            value = nums[i]

            if value != 0:
                # swap zero_index any value on non zero value
                any_value = nums[zero_index]
                nums[zero_index] = value
                nums[i] = any_value
                zero_index += 1
