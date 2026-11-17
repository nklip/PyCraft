from algs.list_node import ListNode

# LeetCode 83: Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Task: Remove repeated values from a sorted singly linked list, retaining one
# node for each distinct value. Relink the existing nodes and return the head
# of the resulting sorted list, or None for an empty input.
class Solution:
    # Time Complexity: O(n), with duplicate runs skipped once by the helper.
    # Space Complexity: O(1), using pointers and reusing the retained nodes.
    # n = number of nodes in the original list.
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        root = head

        while head is not None and head.next is not None:
            if head.val == head.next.val:
                head.next = self.findNextValue(head.next, head.val)
            else:
                head = head.next

        return root

    def findNextValue(self, head: ListNode, oldValue: int) -> ListNode:
        while head.next is not None:
            head = head.next

            if head.val != oldValue:
                return head
        return head.next
