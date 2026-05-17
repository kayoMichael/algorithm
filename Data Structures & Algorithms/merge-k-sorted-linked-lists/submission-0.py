# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        output = ListNode()
        dummyhead = output
        for index, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, index, l))


        while heap:
            val, index, lst = heapq.heappop(heap)
            dummyhead.next = lst
            lst = lst.next
            dummyhead = dummyhead.next
            
            if lst:
                heapq.heappush(heap, (lst.val, index, lst))

        
        return output.next

            
