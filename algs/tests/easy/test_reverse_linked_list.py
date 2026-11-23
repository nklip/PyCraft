import unittest

from algs.easy.reverse_linked_list import Solution
from algs.list_node import ListNode


class TestReverseLinkedList(unittest.TestCase):
    def test_reverses_five_nodes(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

        self._assert_list_values(Solution().reverseList(head), [5, 4, 3, 2, 1])

    def test_reverses_two_nodes(self):
        head = ListNode(1, ListNode(2))

        self._assert_list_values(Solution().reverseList(head), [2, 1])

    def test_empty_list(self):
        self.assertIsNone(Solution().reverseList(None))

    def _assert_list_values(self, node, expected_values):
        for value in expected_values:
            self.assertIsNotNone(node)
            self.assertEqual(node.val, value)
            node = node.next
        self.assertIsNone(node)


if __name__ == "__main__":
    unittest.main()
