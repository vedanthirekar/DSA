# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # new_list = ListNode()
        if not lists:
            return None

        while len(lists)>1:
            list1 = lists.pop()
            list2 = lists.pop()
            new_list = self.mergetwolists(list1,list2)
            lists.append(new_list)

        return lists[-1]

    
    def mergetwolists(self, list1, list2):
        dummy = ListNode()
        curr = dummy
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val<=curr2.val:
                curr.next = curr1
                curr = curr.next
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr = curr.next
                curr2 = curr2.next

        if curr1:
            curr.next = curr1
        else:
            curr.next = curr2

        return dummy.next

    
    

        