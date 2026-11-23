from algs.list_node import ListNode

# LeetCode 206: Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/
# Task: Reverse a singly linked list and return its new head, or None for an
# empty input. This implementation reverses the links of the existing nodes
# in place, making the original tail the new head.
class Solution:
    # Time Complexity: O(n), visiting each node once to reverse its next link.
    # Space Complexity: O(1), reusing nodes with a constant number of pointers.
    # n = number of nodes in the input list.
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        temp = None
        prev = None
        curr = head

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
