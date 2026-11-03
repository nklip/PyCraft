import unittest

from algs.easy.binary_tree_postorder_traversal import Solution
from algs.tree_node import TreeNode


class TestBinaryTreePostorderTraversal(unittest.TestCase):
    def test_right_child_with_left_child(self):
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))

        self.assertEqual(Solution().postorderTraversal(root), [3, 2, 1])

    def test_multiple_branches(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
            TreeNode(3, None, TreeNode(8, TreeNode(9))),
        )

        self.assertEqual(
            Solution().postorderTraversal(root), [4, 6, 7, 5, 2, 9, 8, 3, 1]
        )

    def test_empty_tree(self):
        self.assertEqual(Solution().postorderTraversal(None), [])

    def test_single_node(self):
        self.assertEqual(Solution().postorderTraversal(TreeNode(1)), [1])


if __name__ == "__main__":
    unittest.main()
