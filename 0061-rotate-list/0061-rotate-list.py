# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """brute force sol would be to rotates one element at a time 
        i.e. last element to first, but it will be O(n*k).
        Other solution is to somehow keep the pointer at n-k th position and then
        attach the next part to start. 
        we can try to do that with some method like maintining max x distacne between curr(which will 
        be at the end at the end of iteration) and some pivot variable"""

        curr = head
        pivot = head
        dist = 0
        n = 0
        count_curr = head
        while count_curr:
            count_curr = count_curr.next
            n +=1
        
        if not head or k%n ==0:
            return head

        k = k%n

        while curr.next:
            curr = curr.next
            dist +=1
            if dist>k:
                pivot = pivot.next

        temp = pivot.next
        pivot.next = None
        curr.next = head
        return temp
            