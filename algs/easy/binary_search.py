# LeetCode 704: Binary Search
# https://leetcode.com/problems/binary-search/description/
# Task: Locate target in nums, an ascending list of distinct integers.
# Return its index if found, or -1 if absent. The search must take O(log n) time.
class Solution:
    # Time Complexity: O(log n), halving the search interval at each step.
    # Space Complexity: O(1), using only indices and the current value.
    # n = len(nums).
    def search(self, nums: list[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            mid_index = right_index - (right_index - left_index) // 2

            value = nums[mid_index]

            if value == target:
                return mid_index
            elif value > target:
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1

        return -1
