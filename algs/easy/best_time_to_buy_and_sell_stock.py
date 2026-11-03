# LeetCode 121: Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Task: From the daily prices, find the largest profit from buying one share
# and selling it on a later day. Return 0 when no profitable trade is possible.
class Solution:
    # Time Complexity: O(n), scanning the prices and then the stored profits.
    # Space Complexity: O(n), for the profits list.
    # n = len(prices).
    def maxProfit(self, prices: list[int]) -> int:
        # unlike Java arrays, Python lists can still grow or shrink
        profits = [0] * (len(prices) - 1)

        smallest = -1
        max_so_far = 0

        for price in prices:
            if (smallest == -1):
                smallest = price
            elif smallest > price:
                smallest = price
            elif smallest < price:
                profits[max_so_far] = price - smallest
                max_so_far += 1

        max_profit = 0

        for profit in profits:
            if max_profit < profit:
                max_profit = profit

        return max_profit
