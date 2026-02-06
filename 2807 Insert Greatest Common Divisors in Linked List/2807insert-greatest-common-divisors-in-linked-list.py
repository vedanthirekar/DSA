# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(v1, v2):
            if v2 == 0:
                return v1
            else:
                return gcd(v2,v1%v2)
        
        curr = head
        while curr and curr.next:
            gcd1 = gcd(curr.val, curr.next.val)
            gcdnode = ListNode(gcd1)
            t = curr.next
            curr.next = gcdnode
            gcdnode.next = t
            curr = curr.next.next

        return head 