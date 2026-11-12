import unittest

from algs.easy.maximum_depth_of_binary_tree import Solution
from algs.tree_node import TreeNode


class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    def test_three_level_tree(self):
        root = TreeNode(
            3,
            TreeNode(9),
            TreeNode(20, TreeNode(15), TreeNode(7)),
        )

        self.assertEqual(Solution().maxDepth(root), 3)

    def test_root_with_only_right_child(self):
        root = TreeNode(1, right=TreeNode(2))

        self.assertEqual(Solution().maxDepth(root), 2)


if __name__ == "__main__":
    unittest.main()
