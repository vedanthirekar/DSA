class Solution:
    def rob(self, nums: List[int]) -> int:
        """at each step we can either rob the house or not rob the house. 
        we try to take the max of both. then we try to optimize this
        """
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n<0:
                return 0
            memo[n] =  max(dfs(n-1), dfs(n-2)+nums[n])
            return memo[n]

        n = len(nums)
        return dfs(n-1)