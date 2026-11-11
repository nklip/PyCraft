# LeetCode 643: Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/description/
# Task: Return the largest average among all contiguous portions of nums that
# contain exactly k elements, where 1 <= k <= len(nums).
class Solution:
    # Time Complexity: O(n), updating the sliding sum once per element.
    # Space Complexity: O(1), storing the running sum, best average, and indices.
    # n = len(nums); the window is tracked without copying its k elements.
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        k_sum = 0
        max_average = 0.0
        is_average_set = False

        for i in range(len(nums)):
            value = nums[i]

            if i >= k:
                k_sum -= nums[i - k]
            k_sum += value

            if i + 1 >= k:
                average = k_sum / k

                if is_average_set is False or max_average < average:
                    is_average_set = True
                    max_average = average

        return max_average
