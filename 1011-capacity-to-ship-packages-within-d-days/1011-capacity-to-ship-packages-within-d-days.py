class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """get lowest possible and highest possible val, and apply binary search"""

        l = max(weights)
        h = sum(weights)

        while l<h:
            m = l + (h-l)//2
            if self.check(m, days, weights):
                h = m
            else:
                l = m+1
        
        return h
    
    def check(self, n, days, weights):
        days_left = days
        summ = 0
        for w in weights:
            if summ+w>n:
                days_left -=1
                summ = w 
            else:
                summ += w
        
        return days_left>0