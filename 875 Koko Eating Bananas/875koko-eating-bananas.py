class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        count = 0

        def kworks(k):
            count = 0
            for p in piles:
                count += ceil(p/k)
            return count<=h

        while l<r:
            m = l + (r-l)//2

            if kworks(m):
                r = m
            else:
                l = m+1

        return l