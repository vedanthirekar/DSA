# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        l3 = ListNode()
        curr3 = l3
        carry = 0
        while curr1 or curr2 or carry:
            
            val1 = curr1.val if curr1 else 0 
            val2 = curr2.val if curr2 else 0 
            add = val1+val2+carry
            new_val = add%10 

            new_node = ListNode()
            curr3.next = new_node
            curr3 = curr3.next
            curr3.val = new_val

            carry = add//10

            curr1= curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            

        return l3.next
            
            
        
            
