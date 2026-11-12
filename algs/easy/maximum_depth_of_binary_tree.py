from algs.tree_node import TreeNode

# LeetCode 104: Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Task: Return the greatest number of nodes on any path from the root to a leaf.
# A tree containing only its root has depth 1; an empty tree has depth 0.
class Solution:
    # Time Complexity: O(n), visiting every node once.
    # Space Complexity: O(h), for recursion; O(n) for a skewed tree.
    # n = number of nodes, h = tree height.
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        return self.findMaxDepth(root, 1)

    def findMaxDepth(self, root: TreeNode, maxDepth: int) -> int:
        depth = maxDepth

        if root.left is not None:
            temp = self.findMaxDepth(root.left, maxDepth + 1)

            if temp > depth:
                depth = temp

        if root.right is not None:
            temp = self.findMaxDepth(root.right, maxDepth + 1)

            if temp > depth:
                depth = temp

        return depth
