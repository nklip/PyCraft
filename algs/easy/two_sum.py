class Solution:

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # create dict
        seen = {}
        # normal for only gives you values
        for index, value in enumerate(nums):
            needed = target - value
            # if found - we got our pair of indexes
            if needed in seen:
                return [seen[needed], index]
            # not found - put value with the index in dict
            seen[value] = index
        return [0]
