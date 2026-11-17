import unittest

from algs.easy.remove_duplicates_from_sorted_list import Solution
from algs.list_node import ListNode


class TestRemoveDuplicatesFromSortedList(unittest.TestCase):
    def test_removes_duplicate_at_start(self):
        head = ListNode(1, ListNode(1, ListNode(2)))

        result = Solution().deleteDuplicates(head)

        self._assert_list_values(result, [1, 2])

    def test_removes_duplicates_at_start_and_end(self):
        head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

        result = Solution().deleteDuplicates(head)

        self._assert_list_values(result, [1, 2, 3])

    def _assert_list_values(self, node, expected_values):
        for value in expected_values:
            self.assertIsNotNone(node)
            self.assertEqual(node.val, value)
            node = node.next
        self.assertIsNone(node)


if __name__ == "__main__":
    unittest.main()
