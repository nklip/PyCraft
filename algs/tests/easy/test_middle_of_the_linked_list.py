import unittest

from algs.easy.middle_of_the_linked_list import Solution
from algs.list_node import ListNode


class TestMiddleOfTheLinkedList(unittest.TestCase):
    def test_odd_length_returns_middle_node(self):
        middle = ListNode(3, ListNode(4, ListNode(5)))
        head = ListNode(1, ListNode(2, middle))

        result = Solution().middleNode(head)

        self.assertIs(result, middle)
        self._assert_list_values(result, [3, 4, 5])

    def test_even_length_returns_second_middle_node(self):
        middle = ListNode(4, ListNode(5, ListNode(6)))
        head = ListNode(1, ListNode(2, ListNode(3, middle)))

        result = Solution().middleNode(head)

        self.assertIs(result, middle)
        self._assert_list_values(result, [4, 5, 6])

    def _assert_list_values(self, node, expected_values):
        for value in expected_values:
            self.assertIsNotNone(node)
            self.assertEqual(node.val, value)
            node = node.next
        self.assertIsNone(node)


if __name__ == "__main__":
    unittest.main()
