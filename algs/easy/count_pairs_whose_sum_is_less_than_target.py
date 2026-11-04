# LeetCode 2824: Count Pairs Whose Sum is Less than Target
# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/
# Task: Count index pairs (i, j) with i < j whose values sum to less than target.
# Count each pair of indices once, even when different pairs have equal values.
class Solution:
    # Time Complexity: O(n^2), checking all n * (n - 1) / 2 index pairs.
    # Space Complexity: O(1), using only loop indices, values, and a counter.
    # n = len(nums).
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0

        for i in range(len(nums)):
            i_value = nums[i]
            for k in range(i + 1, len(nums)):
                k_value = nums[k]

                sum = i_value + k_value

                if (sum < target):
                    if (sum < target):
                        count += 1

        return count
