class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        h = num
        
        while l<=h:
            m = l + (h-l)//2

            if m*m == num:
                return True
            elif m*m < num:
                l = m+1
            else:
                h = m-1
        return False
        
        