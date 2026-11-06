import unittest

from algs.easy.intersection_of_two_linked_lists import Solution
from algs.list_node import ListNode


class TestIntersectionOfTwoLinkedLists(unittest.TestCase):
    def test_intersection_at_eight(self):
        shared = ListNode(8, ListNode(4, ListNode(5)))
        head_a = ListNode(4, ListNode(1, shared))
        head_b = ListNode(5, ListNode(6, ListNode(1, shared)))

        self.assertIs(Solution().getIntersectionNode(head_a, head_b), shared)

    def test_intersection_at_two(self):
        shared = ListNode(2, ListNode(4))
        head_a = ListNode(1, ListNode(9, ListNode(1, shared)))
        head_b = ListNode(3, shared)

        self.assertIs(Solution().getIntersectionNode(head_a, head_b), shared)

    def test_no_intersection(self):
        head_a = ListNode(2, ListNode(6, ListNode(4)))
        head_b = ListNode(1, ListNode(5))

        self.assertIsNone(Solution().getIntersectionNode(head_a, head_b))


if __name__ == "__main__":
    unittest.main()
