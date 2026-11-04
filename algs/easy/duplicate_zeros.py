# LeetCode 1089: Duplicate Zeros
# https://leetcode.com/problems/duplicate-zeros/description/
# Task: Insert an extra zero after each original zero in arr, shifting later
# values to the right. Keep the original length by discarding overflow at the
# end. Modify arr in place and return nothing.
class Solution:
    # Time Complexity: O(n), counting zeros and then copying values backward.
    # Space Complexity: O(1) auxiliary space, using only counters and indices.
    # n = len(arr).
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = 0

        for value in arr:
            if value == 0:
                zeros += 1

        read_index = len(arr) - 1
        write_index = len(arr) + zeros - 1

        while read_index >= 0:
            value = arr[read_index]

            # copy any value
            if write_index < len(arr):
                arr[write_index] = value

            # if value is 0, add extra 0
            if value == 0:
                write_index -= 1
                if write_index < len(arr):
                    arr[write_index] = 0

            read_index -= 1
            write_index -= 1
