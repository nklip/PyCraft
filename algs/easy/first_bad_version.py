# LeetCode 278: First Bad Version
# https://leetcode.com/problems/first-bad-version/description/
# Task: Find the earliest bad version among versions 1 through n using
# isBadVersion checks. At least one version is bad, and every version after it
# is also bad. Minimize the number of checks.
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:

    bad = 0

    def __init__(self, bad:int):
        self.bad = bad

    def isBadVersion(self, version: int) -> bool:
        return self.bad <= version

    # Time Complexity: O(log n), halving the interval with one API call per step.
    # Space Complexity: O(log n), for the recursive binary-search stack.
    # n = number of versions; each isBadVersion call is assumed to take O(1).
    def firstBadVersion(self, n: int) -> int:
        return self._firstBadVersion(1, n, -1)

    def _firstBadVersion(self, min: int, max: int, prevBadVersion: int) -> int:
        mid = min + (max - min) // 2

        if self.isBadVersion(mid):
            if max - min == 1 or max - min == 0:
                return mid
            # first bad version could be earlier
            return self._firstBadVersion(min, mid - 1, mid)
        elif prevBadVersion > -1:
            # first bad version was earlier
            if max - min == 1 or max - min == 0:
                return prevBadVersion
            else:
                return self._firstBadVersion(mid + 1, max, prevBadVersion)
        else:
            # first bad version should be later
            return self._firstBadVersion(mid + 1, max, -1)

