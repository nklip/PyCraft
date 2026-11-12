# LeetCode 2540: Minimum Common Value
# https://leetcode.com/problems/minimum-common-value/description/
# Task: Find the smallest integer present in both nonempty lists nums1 and nums2,
# which are sorted in non-decreasing order. Return -1 if they share no value.
class Solution:
    # Time Complexity: O(m + n), comparing current values in at most m + n loop steps.
    # Space Complexity: O(1), using indices and current values only.
    # m = len(nums1), n = len(nums2).
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:

        if nums1[len(nums1) - 1] < nums2[0]:
            return -1
        if nums2[len(nums2) - 1] < nums1[0]:
            return -1

        n1 = 0
        n2 = 0

        length = len(nums1) + len(nums2)

        for i in range(length):

            num1_val = nums1[n1]
            num2_val = nums2[n2]

            if num1_val == num2_val:
                return num1_val
            elif num1_val < num2_val:
                if n1 + 1 != len(nums1):
                    n1 += 1
            else:
                if n2 + 1 != len(nums2):
                    n2 += 1
        return -1
