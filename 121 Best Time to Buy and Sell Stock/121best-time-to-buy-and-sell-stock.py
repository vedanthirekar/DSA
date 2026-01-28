class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        min_price = float("inf")

        for i in prices:
            if i<min_price:
                min_price = i
            diff = max(diff,(i-min_price))

        return diff
        

                

        