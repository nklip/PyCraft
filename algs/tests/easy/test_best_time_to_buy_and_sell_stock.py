import unittest

from algs.easy.best_time_to_buy_and_sell_stock import Solution


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def test_buy_before_selling_for_max_profit(self):
        self.assertEqual(Solution().maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_decreasing_prices_give_no_profit(self):
        self.assertEqual(Solution().maxProfit([7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    unittest.main()
