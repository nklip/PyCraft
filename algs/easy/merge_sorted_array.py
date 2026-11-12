# LeetCode 88: Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/description/
# Task: Merge the first m sorted values of nums1 with the n sorted values of
# nums2, keeping the combined values in non-decreasing order inside nums1.
# Its final n slots provide spare capacity and are not input values. Modify
# nums1 in place and return nothing.
class Solution:
    # Time Complexity: O(m + n) worst case, filling nums1 from the end.
    # Space Complexity: O(1) auxiliary space, using nums1's existing capacity.
    # m = initial valid elements in nums1, n = len(nums2); len(nums1) = m + n.
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 # last real element in nums1 array
        j = n - 1 # last real element in nums2 array
        nums1_lenght = len(nums1) - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                # copy last number from num1
                nums1[nums1_lenght] = nums1[i]
                i -= 1
            else:
                # copy last number from num2
                nums1[nums1_lenght] = nums2[j]
                j -= 1
            nums1_lenght -= 1
