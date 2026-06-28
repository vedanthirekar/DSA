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

        curr = head 
        oldtonew = {}
        while curr:
            curr_new = Node(x =curr.val)
            oldtonew[curr] = curr_new
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                oldtonew[curr].next = oldtonew[curr.next]
            if curr.random:
                oldtonew[curr].random = oldtonew[curr.random]
            curr = curr.next

        return oldtonew[head]
