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
        dictionary = {}

        curr = head

        while curr:
            dictionary[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            node = dictionary[curr]
            if curr.next:
                node.next = dictionary[curr.next]

            if curr.random:
                node.random = dictionary[curr.random]

            curr = curr.next

        return dictionary[head]
        

        