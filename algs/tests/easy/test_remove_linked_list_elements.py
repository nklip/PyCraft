import unittest

from algs.easy.remove_linked_list_elements import Solution
from algs.list_node import ListNode


class TestRemoveLinkedListElements(unittest.TestCase):
    def test_removes_matching_nodes_in_middle_and_at_end(self):
        head = ListNode(
            1,
            ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))),
        )

        result = Solution().removeElements(head, 6)

        for expected in [1, 2, 3, 4, 5]:
            self.assertIsNotNone(result)
            self.assertEqual(result.val, expected)
            result = result.next
        self.assertIsNone(result)

    def test_empty_list(self):
        self.assertIsNone(Solution().removeElements(None, 1))

    def test_removes_all_nodes(self):
        head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))

        self.assertIsNone(Solution().removeElements(head, 7))


if __name__ == "__main__":
    unittest.main()
