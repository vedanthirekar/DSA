class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        l = 1
        r = max(piles)

        while l<=r:
            mid = l + (r-l)//2
            count = 0
            for pile in piles:
                time = math.ceil(pile/mid)
                count += time

            if count<=h:
                r = mid-1
            else:
                l = mid+1

        return l  
            