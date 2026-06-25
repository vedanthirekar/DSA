class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0]
        memo = {}
        n = len(cost)
        def dfs(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            min_cost = min(cost[i]+dfs(i+1), cost[i]+dfs(i+2)) 
            memo[i] = min_cost
            return min_cost

        return min(dfs(0), dfs(1))
