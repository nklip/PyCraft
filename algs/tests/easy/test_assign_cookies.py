import unittest

from algs.easy.assign_cookies import Solution


class TestAssignCookies(unittest.TestCase):
    def test_only_one_child_is_content(self):
        self.assertEqual(Solution().findContentChildren([1, 2, 3], [1, 1]), 1)

    def test_all_children_are_content(self):
        self.assertEqual(Solution().findContentChildren([1, 2], [1, 2, 3]), 2)


if __name__ == "__main__":
    unittest.main()
