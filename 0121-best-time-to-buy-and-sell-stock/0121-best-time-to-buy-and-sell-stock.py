class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        curr_min = float("inf")
        
        #iterating through prices
        for price in prices:
            if price<curr_min:
                curr_min = price

            else:
                max_profit = max(max_profit, price-curr_min)

        return max_profit