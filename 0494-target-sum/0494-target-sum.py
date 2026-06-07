class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dfs(curr_sum, i):
            if (curr_sum,i) in memo:
                return memo[(curr_sum,i)]
            if i == n:
                if curr_sum == target:
                    return 1
                else:
                    return 0
            
            memo[(curr_sum,i)] = dfs(curr_sum+nums[i], i+1) + dfs(curr_sum-nums[i], i+1)
            return memo[(curr_sum,i)]

        return dfs(0, 0 )