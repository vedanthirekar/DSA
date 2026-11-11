class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        
        total_cost = 0
        
        total_cost += min(costBoth, cost1+cost2)* min(need1,need2)

        total_cost += min(costBoth, cost1) * (need1-min(need1, need2))

        total_cost += min(costBoth, cost2) * (need2-min(need1, need2))

        return total_cost