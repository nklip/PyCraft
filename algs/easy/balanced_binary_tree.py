from algs.tree_node import TreeNode

# LeetCode 110: Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/description/
# Task: Check whether every node's left and right subtree heights differ by
# at most one. Return True for a height-balanced tree, including an empty tree.
class Solution:
    # Time Complexity: O(n), visiting each node once.
    # Space Complexity: O(h), for recursion; O(n) for a skewed tree.
    # n = number of nodes, h = tree height.
    def isBalanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        left_depth = self.maxSubtreeDepth(root.left, 1)
        right_depth = self.maxSubtreeDepth(root.right, 1)

        if left_depth is -1 or right_depth is -1:
            return False

        diff = abs(left_depth - right_depth)
        return diff < 2;

    def maxSubtreeDepth(self, root: TreeNode, depth: int):
        left_depth = depth
        right_depth = depth

        if root is not None:
            left_depth = self.maxSubtreeDepth(root.left, depth + 1)
            right_depth = self.maxSubtreeDepth(root.right, depth + 1)

            diff = abs(left_depth - right_depth)

            if diff > 1:
                return -1

        return max(left_depth, right_depth)

