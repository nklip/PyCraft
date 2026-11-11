import unittest

from algs.easy.linked_list_cycle import Solution
from algs.list_node import ListNode


class TestLinkedListCycle(unittest.TestCase):
    def test_tail_connects_to_second_node(self):
        head = ListNode(3)
        second = ListNode(2)
        third = ListNode(0)
        tail = ListNode(-4)
        head.next = second
        second.next = third
        third.next = tail
        tail.next = second

        self.assertTrue(Solution().hasCycle(head))

    def test_tail_connects_to_head(self):
        head = ListNode(1)
        tail = ListNode(2)
        head.next = tail
        tail.next = head

        self.assertTrue(Solution().hasCycle(head))

    def test_single_node_without_cycle(self):
        head = ListNode(1)

        self.assertFalse(Solution().hasCycle(head))


if __name__ == "__main__":
    unittest.main()
