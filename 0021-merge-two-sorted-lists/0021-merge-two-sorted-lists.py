# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        curr3 = d
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val<=curr2.val:
                curr3.next = curr1
                curr3 = curr1
                curr1 = curr1.next
            else:
                curr3.next = curr2
                curr3 = curr2
                curr2 = curr2.next


        if curr1:
            curr3.next = curr1
        elif curr2:
            curr3.next = curr2

        return d.next
