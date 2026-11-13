# LeetCode 2379: Minimum Recolors to Get K Consecutive Black Blocks
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/
# Task: In blocks, 'W' denotes white and 'B' denotes black. Return the fewest
# white-to-black recolorings needed to create a run of at least k black blocks.
# Return 0 if such a run already exists.
class Solution:
    # Time Complexity: O(n), updating the sliding window's black count once per block.
    # Space Complexity: O(1), keeping counters without copying any window.
    # n = len(blocks), 1 <= k <= n.
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blacks = 0
        max_blacks = 0

        for i in range(len(blocks)):
            adding_char = blocks[i]

            if i >= k:
                removing_char = blocks[i - k]

                if removing_char == 'B':
                    blacks -= 1

            if adding_char == 'B':
                blacks += 1

                if max_blacks < blacks:
                    max_blacks = blacks

        return max(k - max_blacks, 0)
