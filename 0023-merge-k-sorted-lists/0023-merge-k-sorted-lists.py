# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergetwo(l1,l2):
            dummy = ListNode()
            d = dummy
            curr1 = l1
            curr2 = l2
            while curr1 and curr2:
                if curr1.val<=curr2.val:
                    d.next = curr1
                    curr1 = curr1.next
                else:
                    d.next = curr2
                    curr2 = curr2.next
                d = d.next

            if curr1:
                d.next = curr1
            else:
                d.next = curr2
            return dummy.next

        n = len(lists)
        if not lists:
            return None
        if n<2:
            return lists[0]
        l1 = lists[0]
        for i in range(1,n):
            l1 = mergetwo(l1,lists[i])

        return l1


        

