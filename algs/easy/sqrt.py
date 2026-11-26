# LeetCode 69: Sqrt(x)
# https://leetcode.com/problems/sqrtx/description/
# Task: Return the square root of a nonnegative integer x rounded down, without
# using built-in exponentiation. This implementation selects an initial guess,
# refines it with Babylonian updates, and truncates the resulting approximation.
class Solution:
    # Time Complexity: O(1), with a fixed cap of 16 Babylonian updates.
    # Space Complexity: O(1), storing a constant number of numeric values.
    # Assumes the task's input range 0 <= x <= 2**31 - 1.
    def mySqrt(self, x: int) -> int:
        seed = 0.0

        if x < 100:
            seed = 2
        elif x < 1000:
            seed = 10
        elif x < 10000:
            seed = 50
        elif x < 100000:
            seed = 200
        elif x < 1000000:
            seed = 1000
        else:
            seed = 50000

        max_iterations = 15
        precision = 10 * (-10)

        while abs(x - seed * seed) > precision:
            # Babylonian Method
            seed = (seed + (x / seed)) / 2

            max_iterations -= 1

            if max_iterations < 0:
                break

        return int(seed)
