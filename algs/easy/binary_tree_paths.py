from algs.tree_node import TreeNode

# LeetCode 257: Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/description/
# Task: For a nonempty binary tree, list every path from the root to a node
# without children. Represent each path as values joined by '->'; the order
# of the returned paths does not matter.
class Solution:
    # Time Complexity: O(n * h), copying path prefixes; O(n^2) for a skewed tree.
    # Space Complexity: O(h^2 + p), for active path strings and returned paths.
    # n = number of nodes, h = tree height, p = total characters in the output.
    # Node values have bounded length under the problem's constraints.
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        result = []

        if self.isLeaf(root):
            result.append(str(root.val))
        else:
            self.collect_root_to_leaf_paths(result, str(root.val), root.left)
            self.collect_root_to_leaf_paths(result, str(root.val), root.right)

        return result

    def collect_root_to_leaf_paths(self, list: list, path_so_far: str, root: TreeNode):
        if root is None:
            return
        path_so_far += f"->{root.val}"

        if self.isLeaf(root):
            list.append(path_so_far)
            return

        if root.left is not None:
            self.collect_root_to_leaf_paths(list, path_so_far, root.left)
        if root.right is not None:
            self.collect_root_to_leaf_paths(list, path_so_far, root.right)

    def isLeaf(self, root: TreeNode):
        return root.left is None and root.right is None
