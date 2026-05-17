# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        second_half_start = None

        while second_half:
            next_node = second_half.next
            second_half.next = second_half_start
            second_half_start = second_half
            second_half = next_node

        curr = head
        dummyhead = ListNode(None)
        output = dummyhead
        while second_half_start and curr:
            dummyhead.next = curr
            curr = curr.next
            dummyhead = dummyhead.next

            dummyhead.next = second_half_start
            second_half_start = second_half_start.next
            dummyhead = dummyhead.next


        if second_half_start:
            dummyhead.next = second_half_start

        else:
            dummyhead.next = curr