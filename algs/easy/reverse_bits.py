# LeetCode 190: Reverse Bits
# https://leetcode.com/problems/reverse-bits/description/
# Task: Reverse the order of all 32 bits of the nonnegative integer n, including
# leading zero bits. Return the integer represented by the reversed bit pattern.
class Solution:
    # Time Complexity: O(1), performing exactly 32 fixed-width bit updates.
    # Space Complexity: O(1), storing the result, remaining input, and loop index.
    # The input and intermediate integers are bounded to 32 bits.
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            # shifts all bits in result one place to the left
            # this makes room on the right to add the next bit
            # so
            # 1) each bit moves left by 1
            # 2) a 0 is added on the right
            # 3) numeric value roughly doubles
            result = result << 1
            # result | thatBit - puts that bit into rightmost position of result
            # |                - is bitwise OR here
            # n & 1            - gets the last bit on n (either 0 or 1)
            # as we appended 0 to the rightmost position in result
            # so result is always 0 for this position
            # The result = result | (n & 1) writes the extracted bit there:
            # if (n & 1) == 0, rightmost stays 0
            # if (n & 1) == 1, rightmost becomes 1
            result = result | (n & 1)
            # unsigned shift:
            # 1) All bits move right by 1
            # 2) The rightmost bit is dropped (that's the one already was read via n & 1)
            # 3) A 0 is inserted on the leftmost side.
            #
            # It consumes bits from right to left, one by one
            #
            # Shift right by one bit; for nonnegative n, zeros are inserted on the left.
            n = n >> 1

        return result
