import unittest

from algs.easy.binary_tree_inorder_traversal import Solution
from algs.tree_node import TreeNode


class TestBinaryTreeInorderTraversal(unittest.TestCase):
    def test_right_child_with_left_child(self):
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))

        self.assertEqual(Solution().inorderTraversal(root), [1, 3, 2])

    def test_tree_with_multiple_levels(self):
        root = TreeNode(
            1,
            TreeNode(
                2,
                TreeNode(4),
                TreeNode(5, TreeNode(6), TreeNode(7)),
            ),
            TreeNode(3, None, TreeNode(8, TreeNode(9))),
        )

        self.assertEqual(
            Solution().inorderTraversal(root), [4, 2, 6, 5, 7, 1, 3, 9, 8]
        )

    def test_empty_tree(self):
        self.assertEqual(Solution().inorderTraversal(None), [])

    def test_single_node(self):
        self.assertEqual(Solution().inorderTraversal(TreeNode(1)), [1])


if __name__ == "__main__":
    unittest.main()
