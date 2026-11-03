import unittest

from algs.easy.binary_tree_preorder_traversal import Solution
from algs.tree_node import TreeNode


class TestBinaryTreePreorderTraversal(unittest.TestCase):
    def test_right_child_with_left_child(self):
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))

        self.assertEqual(Solution().preorderTraversal(root), [1, 2, 3])

    def test_multiple_branches(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
            TreeNode(3, None, TreeNode(8, TreeNode(9))),
        )

        self.assertEqual(
            Solution().preorderTraversal(root), [1, 2, 4, 5, 6, 7, 3, 8, 9]
        )

    def test_empty_tree(self):
        self.assertEqual(Solution().preorderTraversal(None), [])

    def test_single_node(self):
        self.assertEqual(Solution().preorderTraversal(TreeNode(1)), [1])


if __name__ == "__main__":
    unittest.main()
