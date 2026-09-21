class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False
        if x!=0 and x%10==0:
            return False
        rev = 0
        # num = x
        # t = len(x)
        # print(t)

        while rev<x:
            last_digit = x%10
            rev = (rev*10)+last_digit

            x = x//10

        return rev == x or x == rev//10