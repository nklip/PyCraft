import unittest

from algs.easy.minimum_recolors_to_get_k_consecutive_black_blocks import Solution


class TestMinimumRecolorsToGetKConsecutiveBlackBlocks(unittest.TestCase):
    def test_requires_three_recolors(self):
        self.assertEqual(Solution().minimumRecolors("WBBWWBBWBW", 7), 3)

    def test_consecutive_black_blocks_already_exist(self):
        self.assertEqual(Solution().minimumRecolors("WBWBBBW", 2), 0)


if __name__ == "__main__":
    unittest.main()
