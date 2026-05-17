# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr = c = ListNode()
        while l1 or l2:
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val

            if l2:
                val2 = l2.val

            tot = val1 + val2 + carry

            if tot >= 10:
                carry = 1
                tot = tot - 10

            else:
                carry = 0

            curr.val = tot

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

            if l1 or l2:
                curr.next = ListNode()
                curr = curr.next


        if carry != 0:
            curr.next = ListNode()
            curr.next.val = carry


        return c

            


