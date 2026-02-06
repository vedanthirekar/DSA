# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # curr = head
        d = ListNode()
        d.next = head
        curr1 = d
        curr2 = head
        while curr1 and curr2 and curr2.next:
            if curr1== curr2:
                return True

            curr1 = curr1.next
            curr2 = curr2.next.next

            
        return False
