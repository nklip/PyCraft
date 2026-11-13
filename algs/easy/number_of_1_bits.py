# LeetCode 191: Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/description/
# Task: Count the binary digits equal to 1 in the positive integer n.
# Return this count, also called its Hamming weight.
class Solution:
    # Time Complexity: O(b), converting n to binary text, slicing, and scanning it.
    # Space Complexity: O(b), for the binary string and the slice without '0b'.
    # b = number of binary digits in n; b <= 31 under the problem's constraints.
    def hammingWeight(self, n: int) -> int:
        binary_string = bin(n)[2:]

        result = 0

        for ch in binary_string:
            if ch == '1':
                result += 1

        return result
