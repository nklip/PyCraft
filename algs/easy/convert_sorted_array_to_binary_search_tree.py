from algs.tree_node import TreeNode

# LeetCode 108: Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# Task: Build a height-balanced binary search tree from the strictly increasing
# values in nums and return its root. At each node, the left and right subtree
# heights must differ by at most one.
class Solution:
    # Time Complexity: O(n), creating one node per element using index bounds.
    # Space Complexity: O(n) including the output tree; O(log n) auxiliary stack.
    # n = len(nums); choosing each midpoint keeps the recursion balanced.
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        return self.buildBst(nums, 0, len(nums) - 1)

    def buildBst(self, nums: list[int], left: int, right: int):
        if left > right:
            return None

        mid = left + (right - left) // 2

        node = TreeNode(nums[mid])

        node.left = self.buildBst(nums, left, mid - 1)
        node.right = self.buildBst(nums, mid+1, right)

        return node
