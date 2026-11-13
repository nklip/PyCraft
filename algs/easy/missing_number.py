# LeetCode 268: Missing Number
# https://leetcode.com/problems/missing-number/description/
# Task: nums contains n distinct integers drawn from 0 through n inclusive.
# Return the single value from that range that does not appear in nums.
class Solution:
    # Time Complexity: O(n), placing values at matching indices and scanning once.
    # Each swap permanently places a value, so there are at most n swaps in total.
    # Space Complexity: O(1), using indices and temporary values for in-place swaps.
    # n = len(nums); the placement pass reorders the input list.
    def missingNumber(self, nums: list[int]) -> int:
        i = 0

        length = len(nums)

        while i < length:
            value = nums[i]

            if value < length and value != nums[value]:
                # swap
                temp = nums[value]
                nums[value] = value
                nums[i] = temp
            else:
                i += 1

        # find first missing number
        for k in range(length):
            if nums[k] != k:
                return k
        return length
