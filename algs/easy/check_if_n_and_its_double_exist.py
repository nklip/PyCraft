# LeetCode 1346: Check If N and Its Double Exist
# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/
# Task: Determine whether arr contains two values at distinct indices such that
# one is twice the other. A zero can only match another zero at a different index.
class Solution:
    # Time Complexity: O(n) average, using two passes and dictionary lookups.
    # Space Complexity: O(n), for the dictionary of values and their indices.
    # n = len(arr); dictionary operations take O(1) on average.
    def checkIfExist(self, arr: list[int]) -> bool:
        dict = {}

        for index, value in enumerate(arr):
            dict[value] = index

        for index, value in enumerate(arr):
            double_value = 2 * value

            if double_value in dict:
                double_index = dict.get(double_value)
                if double_index != index:
                    return True

        return False;
