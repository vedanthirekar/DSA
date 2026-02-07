# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        mid = head

        # if not curr.next.next:
        #     return curr

        while curr and curr.next:
            curr = curr.next.next
            mid = mid.next

        return mid
        