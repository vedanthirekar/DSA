class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def dfs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in memo:
                return memo[i]

            ways = dfs(i+1) + dfs(i+2)
            memo[i]= ways
            return ways
            
        return dfs(0)