class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #bottom-up
        dp = [float("inf")]*(amount+1)
        dp[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i], 1+dp[i-coin])

        return -1 if  dp[amount] == float("inf") else dp[amount]

        
        
        
        
        
        
        
        
        
        
        
        
        
        # memoization
        memo = {}
        def dfs(curr_sum):
            if curr_sum == amount:
                return 0
            if curr_sum > amount:
                return -1
            if curr_sum in memo:
                return memo[curr_sum]
            minn = float("inf")
            for coin in coins:
                if curr_sum+coin<=amount:
                    minn = min(minn, 1+ dfs(curr_sum+coin))
            memo[curr_sum] = minn
            return minn

        res = dfs(0)
        return -1 if res == float("inf") else res