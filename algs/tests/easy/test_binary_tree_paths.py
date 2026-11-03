import unittest

from algs.easy.binary_tree_paths import Solution
from algs.tree_node import TreeNode

class TestBinaryTreePaths(unittest.TestCase):
    def test_tree_with_two_paths(self):
        root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))

        self.assertCountEqual(Solution().binaryTreePaths(root), ["1->2->5", "1->3"])

    def test_single_node(self):
        self.assertEqual(Solution().binaryTreePaths(TreeNode(1)), ["1"])


if __name__ == "__main__":
    unittest.main()
