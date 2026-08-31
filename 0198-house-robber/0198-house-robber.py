class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0]*(n+2)

        # dp[]
        for i in range(n-1, -1, -1):
            print(i)
            dp[i] = max(nums[i]+dp[i+2], dp[i+1])

        return dp[0]


        # #dp cache 
        # n = len(nums)
        # memo = {}
        # def dfs(i):
        #     if i >= n:
        #         return 0

        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
        #     return memo[i]

        # return dfs(0)



        # # recursive 
        # n = len(nums)
        # def dfs(i):
        #     if i >= n:
        #         return 0
            
        #     maxx = max(nums[i] + dfs(i+2), dfs(i+1))
        #     return maxx

        # return dfs(0)