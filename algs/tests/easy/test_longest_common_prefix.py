import unittest

from algs.easy.longest_common_prefix import Solution


class TestLongestCommonPrefix(unittest.TestCase):
    def test_shared_prefix(self):
        self.assertEqual(
            Solution().longestCommonPrefix(["flower", "flow", "flight"]), "fl"
        )

    def test_no_common_prefix(self):
        self.assertEqual(
            Solution().longestCommonPrefix(["dog", "racecar", "car"]), ""
        )


if __name__ == "__main__":
    unittest.main()
