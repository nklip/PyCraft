# LeetCode 169: Majority Element
# https://leetcode.com/problems/majority-element/description/
# Task: Return the value appearing in more than half the positions of nums.
# The input is nonempty and guarantees that such a majority exists, so the
# candidate produced by the voting pass does not need a verification pass.
class Solution:
    # Time Complexity: O(n), making one pass with Boyer-Moore majority voting.
    # Space Complexity: O(1), storing only the candidate and its counter.
    # n = len(nums).
    def majorityElement(self, nums: list[int]) -> int:
        candidate = 0

        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
