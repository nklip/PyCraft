# LeetCode 66: Plus One
# https://leetcode.com/problems/plus-one/description/
# Task: Add one to the integer represented by digits in most-significant-first
# order, with no leading zeros. Return the resulting digits. The input is updated;
# a carry beyond its first digit creates a new, longer result list.
class Solution:
    # Time Complexity: O(n) worst case, propagating a carry through all digits.
    # Space Complexity: O(n) worst case for the new output list and temporary slice;
    # O(1) extra space when no additional leading digit is needed.
    # n = len(digits).
    def plusOne(self, digits: list[int]) -> list[int]:
        new_array = False
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i]

            if digit == 9:
                digits[i] = 0
                if i == 0:
                    new_array = True
            else:
                digits[i] = digit + 1
                break
        if new_array:
            return_array = [0] * (len(digits) + 1)
            return_array[0] = 1
            return_array[1:len(digits)] = digits[:-1]
            return return_array
        return digits
