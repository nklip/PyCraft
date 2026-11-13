# LeetCode 1984: Minimum Difference Between Highest and Lowest of K Scores
# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/
# Task: Choose any k scores from nums to make the gap between the largest and
# smallest selected scores as small as possible. Return that gap; selected
# scores need not be adjacent in the original list.
class Solution:
    # Time Complexity: O(n log n), sorting before checking each k-score window.
    # Space Complexity: O(n) worst case, for Python's sorting workspace.
    # n = len(nums), 1 <= k <= n; sorting modifies the input list.
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()

        min_difference = float("inf")

        for i in range(k-1, len(nums)):
            min_difference = min(min_difference, nums[i] - nums[i - k + 1])
        return min_difference
