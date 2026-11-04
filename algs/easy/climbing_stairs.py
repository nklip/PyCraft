# LeetCode 70: Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/
# Task: Count the distinct ways to climb n steps when each move climbs either
# one or two steps. Different orders of moves count as different ways.
class Solution:
    # Time Complexity: O(n), computing the number of ways for each step once.
    # Space Complexity: O(n), for the list of counts for all steps.
    # n = number of steps; assumes constant-time, fixed-size integer arithmetic.
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        a = [0] * n

        a[0] = 1
        a[1] = 2

        for i in range(2, n):
            a[i] = a[i-1] + a[i-2]
        return a[n-1]
