from algs.tree_node import TreeNode

# LeetCode 226: Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/
# Task: Return a binary tree's mirror image, exchanging left and right children
# at every node. This implementation builds a new tree; an empty tree returns None.
class Solution:
    # Time Complexity: O(n^2) worst case, as list.pop(0) shifts pending nodes.
    # Space Complexity: O(n) for the output tree and O(n) auxiliary list storage.
    # n = number of nodes; a left-skewed tree fills both lists before removals.
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        target_root = TreeNode(root.val)
        return_node = target_root

        source_stack = []
        target_stack = []

        while root is not None or len(source_stack) != 0:
            while root is not None:
                if root.left is not None:
                    target_root.right = TreeNode(root.left.val)
                source_stack.append(root)
                target_stack.append(target_root)

                root = root.left
                target_root = target_root.right

            root = source_stack.pop(0)
            target_root = target_stack.pop(0)

            if root.right is not None:
                target_root.left = TreeNode(root.right.val)

            root = root.right
            target_root = target_root.left

        return return_node
