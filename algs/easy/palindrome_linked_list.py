from algs.list_node import ListNode

# LeetCode 234: Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/description/
# Task: Check whether the values of a singly linked list read identically from
# front to back and back to front. This implementation reverses links from the
# middle onward and leaves those links changed after the check.
class Solution:
    # Time Complexity: O(n), finding the middle, reversing the suffix, and comparing.
    # Space Complexity: O(1), using pointers without copying nodes or their values.
    # n = number of nodes in the list.
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head

        # 1. findthe middle list for slow
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # 2. find the second half of the middle for slow
        prev = None
        while slow is not None:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        # 3. compare head and prev
        left = head
        right = prev
        while right is not None and left is not None:
            if left.val != right.val:
                return False
            right = right.next
            left = left.next
        return True
