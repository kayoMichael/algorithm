# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0 
        curr = head
        while curr:
            curr = curr.next
            length += 1

        if length < k:
            return head

        curr = head
        next_sequence = None
        for t in range(length // k):
            prev = None
            merge_point = curr
            for i in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            if next_sequence:
                next_sequence.next = prev

            if t == 0:
                return_point = prev

            next_sequence = merge_point

        if length % k != 0:
            next_sequence.next = curr
        
        return return_point






