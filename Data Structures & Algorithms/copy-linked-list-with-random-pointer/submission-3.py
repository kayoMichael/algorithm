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
            if curr not in dictionary:
                dictionary[curr] = Node(curr.val)

            if curr.next and curr.next not in dictionary:
                dictionary[curr.next] = Node(curr.next.val)

            if curr.random and curr.random not in dictionary:
                dictionary[curr.random] = Node(curr.random.val)

            if curr.next:
                dictionary[curr].next = dictionary[curr.next]

            if curr.random:
                dictionary[curr].random = dictionary[curr.random]

            curr = curr.next

        return dictionary[head]