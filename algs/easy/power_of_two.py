# LeetCode 231: Power of Two
# https://leetcode.com/problems/power-of-two/description/
# Task: Return whether n equals 2 raised to a nonnegative integer power.
# One qualifies as 2^0; zero and negative integers do not qualify.
class Solution:
    # Time Complexity: O(1) for the problem's 32-bit integers, using a bitwise check.
    # Space Complexity: O(1) under the same fixed-width bound.
    # For arbitrary-size positive Python integers, both bounds are O(b), where
    # b is the number of binary digits in n, due to subtraction and bitwise AND.
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
