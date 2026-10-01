class Solution:
    def climbStairs(self, n: int) -> int:
        
        # memo = {}
        # def dfs(i):
        #     if i > n:
        #         return 0
        #     if i == n:
        #         return 1
        #     if i in memo:
        #         return memo[i]

        #     ways = dfs(i+1) + dfs(i+2)
        #     memo[i]= ways
        #     return ways
            
        # return dfs(0)


        dp = [0]*(n+1)
        dp[n] = 1
        dp[n-1] = 1
        for i in range(n-2, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]

        return dp[0]