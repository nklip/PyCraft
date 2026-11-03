import unittest

from algs.easy.balanced_binary_tree import Solution
from algs.tree_node import TreeNode


class TestBalancedBinaryTree(unittest.TestCase):
    def test_balanced_tree(self):
        root = TreeNode(
            3,
            TreeNode(9),
            TreeNode(20, TreeNode(15), TreeNode(7)),
        )

        self.assertTrue(Solution().isBalanced(root))

    def test_unbalanced_tree(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
            TreeNode(2),
        )

        self.assertFalse(Solution().isBalanced(root))

    def test_empty_tree(self):
        self.assertTrue(Solution().isBalanced(None))


if __name__ == "__main__":
    unittest.main()
