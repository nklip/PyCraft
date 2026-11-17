# LeetCode 27: Remove Element
# https://leetcode.com/problems/remove-element/description/
# Task: Compact the values unequal to val into the front of nums and return
# their count k. Only nums[:k] is significant; the remaining entries may be
# ignored. This implementation preserves the retained values' original order.
class Solution:
    # Time Complexity: O(n), scanning once and copying each retained value forward.
    # Space Complexity: O(1), using indices and the current value only.
    # n = len(nums); the input list is modified but not resized.
    def removeElement(self, nums: list[int], val: int) -> int:
        output = 0

        for i in range(len(nums)):
            value = nums[i]

            if value != val:
                nums[output] = value
                output += 1
        return output
