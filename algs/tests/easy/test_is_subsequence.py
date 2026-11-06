import unittest

from algs.easy.is_subsequence import Solution


class TestIsSubsequence(unittest.TestCase):
    def test_abc_is_subsequence_of_ahbgdc(self):
        self.assertTrue(Solution().isSubsequence("abc", "ahbgdc"))

    def test_axc_is_not_subsequence_of_ahbgdc(self):
        self.assertFalse(Solution().isSubsequence("axc", "ahbgdc"))


if __name__ == "__main__":
    unittest.main()
