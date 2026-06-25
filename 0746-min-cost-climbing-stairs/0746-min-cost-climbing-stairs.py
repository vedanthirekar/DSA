class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp = [0]*(n+2)
        curr = 0 
        prev = 0

        for i in range(n-1,-1,-1):
            temp = curr
            curr = cost[i]+ min(curr, prev)
            prev = temp


        return min(prev, curr)
        
        
        
        
        
        
        
        
        
        
        
        
        # # min_cost = [0]
        # memo = {}
        # n = len(cost)
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     min_cost = min(cost[i]+dfs(i+1), cost[i]+dfs(i+2)) 
        #     memo[i] = min_cost
        #     return min_cost

        # return min(dfs(0), dfs(1))
