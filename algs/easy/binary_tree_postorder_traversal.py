from algs.tree_node import TreeNode

# LeetCode 145: Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Task: Produce a list of the tree's values in left subtree, right subtree, node
# order. An empty tree produces an empty list.
# Follow-up: Implement the traversal iteratively.
class Solution:
    # Time Complexity: O(n), pushing and popping each node once.
    # Space Complexity: O(n) including output; O(h) auxiliary space for the stack.
    # n = number of nodes, h = tree height (up to n).
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        list = []

        if root is None:
            return list

        stack = []
        last_visited = None

        # left -> right -> root
        while root is not None or len(stack) != 0:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                peek_node = stack[-1]
                if peek_node.right is not None and last_visited is not peek_node.right:
                    root = peek_node.right
                else:
                    # add value if it's a leaf
                    # or all leafs already added
                    list.append(peek_node.val)
                    last_visited = peek_node
                    if len(stack) != 0:
                        stack.pop()

        return list
