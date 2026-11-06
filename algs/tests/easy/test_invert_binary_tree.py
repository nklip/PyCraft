import unittest

from algs.easy.invert_binary_tree import Solution
from algs.tree_node import TreeNode


class TestInvertBinaryTree(unittest.TestCase):
    def test_inverts_three_level_tree(self):
        root = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9)),
        )
        expected = TreeNode(
            4,
            TreeNode(7, TreeNode(9), TreeNode(6)),
            TreeNode(2, TreeNode(3), TreeNode(1)),
        )

        self._assert_tree_equal(Solution().invertTree(root), expected)

    def test_inverts_two_level_tree(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        expected = TreeNode(2, TreeNode(3), TreeNode(1))

        self._assert_tree_equal(Solution().invertTree(root), expected)

    def test_empty_tree(self):
        self.assertIsNone(Solution().invertTree(None))

    def _assert_tree_equal(self, actual, expected):
        if expected is None:
            self.assertIsNone(actual)
            return

        self.assertIsNotNone(actual)
        self.assertEqual(actual.val, expected.val)
        self._assert_tree_equal(actual.left, expected.left)
        self._assert_tree_equal(actual.right, expected.right)


if __name__ == "__main__":
    unittest.main()
