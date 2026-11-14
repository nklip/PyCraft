import unittest

from algs.easy.palindrome_linked_list import Solution
from algs.list_node import ListNode


class TestPalindromeLinkedList(unittest.TestCase):
    def test_palindromic_list(self):
        head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))

        self.assertTrue(Solution().isPalindrome(head))

    def test_non_palindromic_list(self):
        head = ListNode(1, ListNode(2))

        self.assertFalse(Solution().isPalindrome(head))


if __name__ == "__main__":
    unittest.main()
