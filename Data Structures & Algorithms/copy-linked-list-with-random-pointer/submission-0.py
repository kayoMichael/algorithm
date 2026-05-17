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
            return None
        hashmap = {}
        output = head
        while head:
            hashmap[head] = Node(head.val)
            head = head.next



        for real, copy in hashmap.items():
            if real.next:
                copy.next = hashmap[real.next]

            if real.random:
                copy.random = hashmap[real.random]


        return hashmap[output]

            

            
