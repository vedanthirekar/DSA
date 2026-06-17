class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        summ = sum(nums)
        if summ%2!=0:
            return False
        
        target = summ/2
        n = len(nums)

        memo = {}

        def dfs(curr_sum, i):
            if curr_sum == target:
                return True
            if curr_sum >target:
                return False
            if i>=n:
                return False

            if (curr_sum, i) in memo:
                return memo[(curr_sum, i)]
            
            res = dfs(curr_sum+nums[i],i+1) or dfs(curr_sum, i+1)
            memo[(curr_sum, i)] = res
            return res


        return dfs(0, 0)

