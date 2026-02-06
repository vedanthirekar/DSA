# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # n = head
        # s = set()
        # if n:
        #     s.add(n.val)
        # while n and n.next:
        #     if n.next.val not in s:
        #         s.add(n.next.val)
        #         n = n.next
        #     else:
        #         n.next = n.next.next
            
        # return head

        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head