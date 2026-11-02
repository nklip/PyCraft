from algs.list_node import ListNode

class Solution:

    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        root = None
        last = None

        carry = 0

        while l1 is not None or l2 is not None:
            summary = (
                (0 if l1 is None else l1.val) +
                (0 if l2 is None else l2.val) +
                carry
            )

            if summary >= 10:
                summary -= 10
                carry = 1
            else:
                carry = 0

            sumNode = ListNode(summary)

            if root is None:
                root = sumNode
                last = sumNode
            else:
                last.next = sumNode
                last = sumNode

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        if carry > 0:
            last.next = ListNode(carry)

        return root