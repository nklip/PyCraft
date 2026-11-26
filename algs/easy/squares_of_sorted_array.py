# LeetCode 977: Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
# Task: Given nums in nondecreasing order, return its squared values in
# nondecreasing order. Compare squares at both ends and fill a new list from
# largest to smallest, leaving the input unchanged.
class Solution:
    # Time Complexity: O(n), allocating the result and filling each position once.
    # Space Complexity: O(n), for the returned list; O(1) auxiliary space.
    # n = len(nums).
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        result_index = len(nums) - 1

        left = 0
        right = len(nums) - 1

        while left <= right:
            left_value = nums[left]
            right_value = nums[right]

            left_square = left_value * left_value
            right_square = right_value * right_value

            if left_square >= right_square:
                result[result_index] = left_square
                result_index -= 1
                left += 1
            else:
                result[result_index] = right_square
                result_index -= 1
                right -= 1
        return result
