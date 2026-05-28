class Solution:
    def rob(self, nums: List[int]) -> int:
        """at each step we can either rob the house or not rob the house. 
        we try to take the max of both. then we try to optimize this
        """

        n = len(nums)
        # dp = [0]*n
        if len(nums)<2:
            return nums[0]
        
        prev = nums[0]
        curr = max(nums[1],nums[0])

        for i in range(2,n):
            temp = curr
            curr = max(prev+nums[i],curr)
            prev = temp

        return curr















        # #space optimized
        # n = len(nums)
        # if not nums:
        #     return 0
        # if n == 1:
        #     return nums[0]
        # prev = nums[0]
        # curr = max(nums[1],nums[0])
        # res = 0
        # for i in range(2,n):
        #     res = max(prev+nums[i],curr)
            
        #     prev = curr
        #     curr = res
            
        # return curr



        # n = len(nums)
        # if not nums:
        #     return 0
        # if n == 1:
        #     return nums[0]
        # dp = [0]*n
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, n):
        #     dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        # return dp[-1]
        
        
        
        # memo = {}
        # def dfs(n):
        #     if n in memo:
        #         return memo[n]
        #     if n<0:
        #         return 0
        #     memo[n] =  max(dfs(n-1), dfs(n-2)+nums[n])
        #     return memo[n]

        # n = len(nums)
        # return dfs(n-1)



