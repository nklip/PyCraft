# LeetCode 202: Happy Number
# https://leetcode.com/problems/happy-number/description/
# Task: Starting with positive n, repeatedly square each decimal digit and add
# the squares to obtain the next number. Return whether this process reaches 1;
# a repeating cycle that never reaches 1 means the number is not happy.
class Solution:
    # Time Complexity: O(log(n + 1)), dominated by processing the initial digits;
    # subsequent digit-square sums quickly shrink into a fixed bounded range.
    # Space Complexity: O(1), using slow and fast values for cycle detection.
    # n = input integer; assumes constant-time, fixed-size integer arithmetic.
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquares(n)
        while fast != 1 and slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
        return True if fast == 1 else False

    def sumOfSquares(self, n:int) -> int:
        sum = 0

        while n > 0:
            # take the latest int char
            d = n % 10
            # reduce n by 10
            n //= 10
            # find the sum of squares
            sum += d * d

        return sum
