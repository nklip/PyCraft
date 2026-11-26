from algs.tree_node import TreeNode

# LeetCode 100: Same Tree
# https://leetcode.com/problems/same-tree/description/
# Task: Return whether binary trees p and q have identical structure and equal
# values at corresponding nodes. Two empty trees match; a missing node in only
# one tree or unequal node values makes the trees different.
class Solution:
    # Time Complexity: O(n), comparing corresponding nodes at most once.
    # Space Complexity: O(h), for recursion; O(n) in the skewed-tree worst case.
    # n = total nodes in both trees; h = the larger tree height.
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        elif p is not None and q is None:
            return False
        elif p is None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                left_result = self.isSameTree(p.left, q.left)
                right_result = self.isSameTree(p.right, q.right)

                return p.val == q.val and left_result and right_result
