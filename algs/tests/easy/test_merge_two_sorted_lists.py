import unittest

from algs.easy.merge_two_sorted_lists import Solution
from algs.list_node import ListNode


class TestMergeTwoSortedLists(unittest.TestCase):
    def test_merges_two_nonempty_lists(self):
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))

        result = Solution().mergeTwoLists(list1, list2)

        for expected in [1, 1, 2, 3, 4, 4]:
            self.assertIsNotNone(result)
            self.assertEqual(result.val, expected)
            result = result.next
        self.assertIsNone(result)

    def test_both_lists_empty(self):
        self.assertIsNone(Solution().mergeTwoLists(None, None))

    def test_first_list_empty(self):
        result = Solution().mergeTwoLists(None, ListNode(0))

        self.assertIsNotNone(result)
        self.assertEqual(result.val, 0)
        self.assertIsNone(result.next)


if __name__ == "__main__":
    unittest.main()
