from algs.tree_node import TreeNode
from collections import deque

# LeetCode 111: Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Task: Return the fewest nodes needed to travel from the root to any leaf.
# A leaf has neither a left nor a right child. Return 0 for an empty tree.
class Solution:
    # Time Complexity: O(n) worst case, searching level by level to the first leaf.
    # Space Complexity: O(w), for the queue; O(n) in the worst case.
    # n = number of nodes, w = maximum number of nodes on any tree level.
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if node.left is None and node.right is None:
                return depth

            if node.left is not None:
                queue.append((node.left, depth + 1))

            if node.right is not None:
                queue.append((node.right, depth + 1))
