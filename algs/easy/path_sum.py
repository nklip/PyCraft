from algs.tree_node import TreeNode

# LeetCode 112: Path Sum
# https://leetcode.com/problems/path-sum/description/
# Task: Determine whether any path from the root to a leaf has node values that
# add up to targetSum. A leaf has no children; an empty tree has no qualifying path.
class Solution:
    # Time Complexity: O(n), visiting each node and updating the running path sum.
    # Space Complexity: O(h), for recursion; O(n) for a skewed tree.
    # n = number of nodes, h = tree height.
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        return self._hasPathSum(root, targetSum, root.val)

    def _hasPathSum(self, root: TreeNode, targetSum: int, currSum: int) -> bool:
        if self.isLeaf(root) and targetSum == currSum:
            return True
        is_left_path = False
        is_right_path = False

        if root.left is not None:
            this_sum = currSum + root.left.val
            is_left_path = self._hasPathSum(root.left, targetSum, this_sum)
        if root.right is not None:
            this_sum = currSum + root.right.val
            is_right_path = self._hasPathSum(root.right, targetSum, this_sum)
        return is_left_path or is_right_path

    def isLeaf(self, node: TreeNode) -> bool:
        return node.left is None and node.right is None
