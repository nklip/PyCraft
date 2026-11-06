# LeetCode 374: Guess Number Higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
# Task: Find the hidden integer in the inclusive range 1 through n using guess
# feedback: 1 means the hidden number is higher, -1 means lower, and 0 is a match.
class Solution:

    pick = 0

    def __init__(self, guess:int):
        self.pick = guess

    def guess(self, guess:int):
        return (self.pick > guess) - (self.pick < guess)

    # Time Complexity: O(log n), halving the search interval with each guess.
    # Space Complexity: O(log n), for the recursive binary-search stack.
    # n = upper bound of the search range; each guess call is assumed to be O(1).
    def guessNumber(self, n: int) -> int:
        return self._guessNumber(1, n)

    def _guessNumber(self, min:int, max:int):
        mid = max - (max - min) // 2

        comparison = self.guess(mid)

        if comparison == 1:
            return self._guessNumber(mid + 1, max)
        elif comparison == -1:
            return self._guessNumber(min, mid - 1)
        else:
            return mid
