# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        We first find the mid of the list, then reverse the 2nd half.
        Then we merge them together. 
        """
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        pivot = slow.next
        slow.next = None

        curr = pivot
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        l2_head = prev

        curr1 = head
        curr2 = l2_head

        while curr2:
            temp1 = curr1.next
            temp2 = curr2.next
            curr1.next = curr2
            curr1 = temp1
            curr2.next = curr1
            curr2 = temp2

        return curr1





        