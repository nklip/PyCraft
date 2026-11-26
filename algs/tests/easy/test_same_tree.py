import unittest

from algs.easy.same_tree import Solution
from algs.tree_node import TreeNode


class TestSameTree(unittest.TestCase):
    def test_matching_values_and_structure(self):
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))

        self.assertTrue(Solution().isSameTree(p, q))

    def test_different_structure(self):
        p = TreeNode(1, left=TreeNode(2))
        q = TreeNode(1, right=TreeNode(2))

        self.assertFalse(Solution().isSameTree(p, q))

    def test_different_values(self):
        p = TreeNode(1, TreeNode(2), TreeNode(1))
        q = TreeNode(1, TreeNode(1), TreeNode(2))

        self.assertFalse(Solution().isSameTree(p, q))


if __name__ == "__main__":
    unittest.main()
