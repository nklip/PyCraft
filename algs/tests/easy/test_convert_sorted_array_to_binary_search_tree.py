import unittest

from algs.easy.convert_sorted_array_to_binary_search_tree import Solution


class TestConvertSortedArrayToBinarySearchTree(unittest.TestCase):
    def test_sorted_array_with_negative_and_positive_numbers(self):
        nums = [-10, -3, 0, 5, 9]

        root = Solution().sortedArrayToBST(nums.copy())

        self._assert_balanced_bst(root, nums)

    def test_sorted_array_with_two_numbers(self):
        nums = [1, 3]

        root = Solution().sortedArrayToBST(nums.copy())

        self._assert_balanced_bst(root, nums)

    def _assert_balanced_bst(self, root, expected_values):
        values = []

        def visit(node):
            if node is None:
                return 0

            left_height = visit(node.left)
            values.append(node.val)
            right_height = visit(node.right)

            self.assertLessEqual(abs(left_height - right_height), 1)

            return 1 + max(left_height, right_height)

        visit(root)
        self.assertEqual(values, expected_values)


if __name__ == "__main__":
    unittest.main()
