# LeetCode 219: Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/description/
# Task: Return whether nums contains equal values at two distinct indices whose
# distance is at most k. Equal values farther apart do not qualify.
class Solution:
    # Time Complexity: O(n) average, scanning once with set operations.
    # Space Complexity: O(min(n, k + 1)), for the sliding-window set.
    # n = len(nums), k = maximum index distance; set operations average O(1).
    # The set holds up to k previous values plus the current value.
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        sliding_window = set()

        for i, value in enumerate(nums):
            if i > k:
                temp = nums[i - k - 1]
                sliding_window.remove(temp)

            if value in sliding_window:
                return True

            sliding_window.add(value)

        return False
