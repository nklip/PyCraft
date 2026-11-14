import unittest

from algs.easy.path_sum import Solution
from algs.tree_node import TreeNode


class TestPathSum(unittest.TestCase):
    def test_root_to_leaf_path_sums_to_twenty_two(self):
        root = TreeNode(
            5,
            TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
            TreeNode(8, TreeNode(13), TreeNode(4, right=TreeNode(1))),
        )

        self.assertTrue(Solution().hasPathSum(root, 22))

    def test_no_root_to_leaf_path_matches_target(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))

        self.assertFalse(Solution().hasPathSum(root, 5))

    def test_empty_tree_has_no_path(self):
        self.assertFalse(Solution().hasPathSum(None, 0))


if __name__ == "__main__":
    unittest.main()
