from algs.list_node import ListNode

# LeetCode 160: Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Task: Find the first shared node of two acyclic singly linked lists, or return
# None if they do not intersect. Sharing means the same node object, not merely
# equal values. Preserve both lists' links.
class Solution:
    # Time Complexity: O(m + n), with each pointer traversing at most both lists.
    # Space Complexity: O(1), using two pointers without allocating nodes.
    # m = number of nodes in headA, n = number of nodes in headB.
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        a = headA
        b = headB

        while a != b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next

        return a
