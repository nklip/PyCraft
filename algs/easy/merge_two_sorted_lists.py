from algs.list_node import ListNode

# LeetCode 21: Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Task: Combine two singly linked lists sorted in non-decreasing order by
# relinking their existing nodes. Return the merged list's head, or None when
# both inputs are empty.
class Solution:
    # Time Complexity: O(m + n) worst case, selecting one node per recursive call.
    # Space Complexity: O(m + n) worst case, for recursion despite reusing nodes.
    # m = number of nodes in list1, n = number of nodes in list2.
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1 is not None and list2 is not None:
            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
        if list1 is None:
            return list2
        return list1
