"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        curr = head

        while curr:
            next_node = curr.next
            clone = Node(curr.val)
            curr.next = clone
            clone.next = next_node
            curr = next_node

        curr = head

        while curr:
            clone = curr.next
            if curr.random:
                clone.random = curr.random.next
            curr = curr.next.next

        dummyhead = Node(0)
        output = dummyhead
        curr = head
        while curr:
            dummyhead.next = curr.next
            if curr.next:
                curr.next = curr.next.next
            curr = curr.next
            dummyhead = dummyhead.next

        return output.next
        

