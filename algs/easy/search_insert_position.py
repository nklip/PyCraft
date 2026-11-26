# LeetCode 35: Search Insert Position
# https://leetcode.com/problems/search-insert-position/description/
# Task: Given a nonempty list of distinct integers in ascending order, return
# target's index if present, or the index where it would be inserted to keep
# the list sorted. Search by index bounds without modifying nums.
class Solution:
    # Time Complexity: O(log n), halving the search interval at each step.
    # Space Complexity: O(log n), for the recursive binary-search call stack.
    # n = len(nums); the helper passes indices without copying list slices.
    def searchInsert(self, nums: list[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)

    def binarySearch(self, nums: list[int], target: int, lp: int, rp: int) -> int:
        med_id = ((rp - lp) // 2) + lp
        med_value = nums[med_id]

        if med_value == target:
            return med_id
        elif rp - lp <= 2:
            if nums[lp] >= target:
                return lp
            elif nums[rp] == target:
                return rp
            elif nums[rp] < target:
                return rp + 1

        if med_value < target:
            return self.binarySearch(nums, target, med_id + 1, rp)
        else:
            return self.binarySearch(nums, target, lp, med_id)

