import unittest

from algs.easy.isomorphic_strings import Solution


class TestIsomorphicStrings(unittest.TestCase):
    def test_egg_and_add_are_isomorphic(self):
        self.assertTrue(Solution().isIsomorphic("egg", "add"))

    def test_f11_and_b23_are_not_isomorphic(self):
        self.assertFalse(Solution().isIsomorphic("f11", "b23"))

    def test_paper_and_title_are_isomorphic(self):
        self.assertTrue(Solution().isIsomorphic("paper", "title"))


if __name__ == "__main__":
    unittest.main()
