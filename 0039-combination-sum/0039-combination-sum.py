class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        res = []

        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(ans[:])
                return 
            if curr_sum>target:
                return
            
            for i in range(i,len(candidates)):
                ans.append(candidates[i]) 
                dfs(i, curr_sum+candidates[i])
                ans.pop()

        dfs(0, 0)
        return res