class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #dp cache 
        n = len(nums)
        memo = {}
        def dfs(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return memo[i]

        return dfs(0)



        #recursive 
        # n = len(nums)
        # def dfs(i):
        #     if i >= n:
        #         return 0
            
        #     maxx = max(nums[i] + dfs(i+2), dfs(i+1))
        #     return maxx

        # return dfs(0)