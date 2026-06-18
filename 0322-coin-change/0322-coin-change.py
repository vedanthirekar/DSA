class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # minn = 
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