class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEat(k):
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/k)

            return hour<=h

        low = 1
        high = max(piles)

        while low<high:
            mid = low+ (high-low)//2

            if canEat(mid):
                high = mid

            else:
                low = mid+1

        return high

