# LeetCode 136: Single Number
# https://leetcode.com/problems/single-number/description/
# Task: Find the value that appears once in a nonempty list where every other
# value appears exactly twice. XOR all values so each duplicate pair cancels,
# leaving the single unpaired value.
class Solution:
    # Time Complexity: O(n), applying XOR once per element.
    # Space Complexity: O(1), keeping only the accumulator and current value.
    # n = len(nums); integers are bounded by the task's constraints.
    def singleNumber(self, nums: list[int]) -> int:
        result = 0

        for num in nums:
            result ^= num
        return result
