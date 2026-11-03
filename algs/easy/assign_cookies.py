# LeetCode 455: Assign Cookies
# https://leetcode.com/problems/assign-cookies/description/
# Task: Match cookies to children so that as many children as possible receive
# a cookie meeting their minimum size (greed). Each cookie can be used once,
# and each child can receive only one. Return the number of satisfied children.
class Solution:
    # Time Complexity: O(n log n + m log m), dominated by sorting both lists.
    # Space Complexity: O(max(n, m)), for Python's sorting workspace.
    # n = len(greed), m = len(size).
    def findContentChildren(self, greed: list[int], size: list[int]) -> int:
        if greed is None or size is None or len(greed) < 1:
            return 0

        greed.sort()
        size.sort()

        child = 0
        cookie = 0

        while child < len(greed) and cookie < len(size):
            if greed[child] <= size[cookie]:
                child += 1
            cookie += 1

        return child
