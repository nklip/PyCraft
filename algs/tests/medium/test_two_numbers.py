import unittest

from algs.list_node import ListNode
from algs.medium.add_two_numbers import Solution

class AddTwoNumbers(unittest.TestCase):
    def test_two_numbers(self):
        node1 = ListNode(2)
        node2 = ListNode(4)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3

        node4 = ListNode(5)
        node5 = ListNode(6)
        node6 = ListNode(4)
        node4.next = node5
        node5.next = node6

        actualNode = Solution().addTwoNumbers(node1, node4)

        self.assertEqual(actualNode.val, 7)
        self.assertEqual(actualNode.next.val, 0)
        self.assertEqual(actualNode.next.next.val, 8)

    def test_two_numbers_zeros(self):
        node1 = ListNode(0)
        node2 = ListNode(0)

        actualNode = Solution().addTwoNumbers(node1, node2)

        self.assertEqual(actualNode.val, 0)

    def test_two_numbers_nines(self):
        node1 = ListNode(9)
        node2 = ListNode(9)
        node3 = ListNode(9)
        node4 = ListNode(9)
        node5 = ListNode(9)
        node6 = ListNode(9)
        node7 = ListNode(9)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = node7

        node8 = ListNode(9)
        node9 = ListNode(9)
        node10 = ListNode(9)
        node11 = ListNode(9)
        node8.next = node9
        node9.next = node10
        node10.next = node11

        actualNode = Solution().addTwoNumbers(node1, node8)

        self.assertEqual(actualNode.val, 8)
        self.assertEqual(actualNode.next.val, 9)
        self.assertEqual(actualNode.next.next.val, 9)
        self.assertEqual(actualNode.next.next.next.val, 9)
        self.assertEqual(actualNode.next.next.next.next.val, 0)
        self.assertEqual(actualNode.next.next.next.next.next.val, 0)
        self.assertEqual(actualNode.next.next.next.next.next.next.val, 0)
        self.assertEqual(actualNode.next.next.next.next.next.next.next.val, 1)
        self.assertIsNone(actualNode.next.next.next.next.next.next.next.next)
