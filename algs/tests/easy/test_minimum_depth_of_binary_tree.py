import unittest

from algs.easy.minimum_depth_of_binary_tree import Solution
from algs.tree_node import TreeNode


class TestMinimumDepthOfBinaryTree(unittest.TestCase):
    def test_shortest_path_to_leaf(self):
        root = TreeNode(
            3,
            TreeNode(9),
            TreeNode(20, TreeNode(15), TreeNode(7)),
        )

        self.assertEqual(Solution().minDepth(root), 2)

    def test_right_only_chain(self):
        root = TreeNode(
            2,
            right=TreeNode(
                3, right=TreeNode(4, right=TreeNode(5, right=TreeNode(6)))
            ),
        )

        self.assertEqual(Solution().minDepth(root), 5)


if __name__ == "__main__":
    unittest.main()
