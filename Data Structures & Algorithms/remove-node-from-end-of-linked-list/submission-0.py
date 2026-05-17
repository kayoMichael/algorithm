# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyhead = ListNode(None)
        dummyhead.next = head
        slow = dummyhead
        fast = dummyhead
        for _ in range(n):
            fast = fast.next

        itself = False
        while fast.next:
            itself = True
            slow = slow.next
            fast = fast.next

        if itself:
            slow.next = slow.next.next

        else:
            dummyhead.next = dummyhead.next.next

        return dummyhead.next



