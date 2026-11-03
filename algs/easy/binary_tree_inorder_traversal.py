from algs.tree_node import TreeNode

# LeetCode 94: Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Task: Produce a list of the tree's values in left subtree, node, right subtree
# order. An empty tree produces an empty list.
# Follow-up: Implement the traversal iteratively.
class Solution:
    # Time Complexity: O(n), pushing and popping each node once.
    # Space Complexity: O(n) including output; O(h) auxiliary space for the stack.
    # n = number of nodes, h = tree height (up to n).
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        return_list = []

        stack = []

        while root is not None or len(stack) != 0:
            # go left a far as possible
            while root is not None:
                # pull all nodes (including the leaft)
                # in stack along the way
                # till we find the deepest left leaf
                stack.append(root)
                # when root.left is empty we leave the cycle
                root = root.left

            # we go back and start using the last node
            # for example, the deepest left leaf

            root = stack.pop()
            return_list.append(root.val)

            # then we start checking the right path
            root = root.right

        return return_list
