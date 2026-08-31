# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #breaking into half
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        break_pt = slow.next
        slow.next = None

        #reverse 2nd half
        curr = break_pt
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #alternate adding
        curr1 = head
        curr2 = prev

        while curr1 and curr2:
            temp1 = curr1.next
            curr1.next = curr2
            temp2 = curr2.next
            curr2.next = temp1


            curr1 = temp1
            curr2 = temp2