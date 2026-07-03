class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(curr_sum,i,ans):
            if curr_sum == target:
                res.append(ans[:])
                return 
            # if curr_sum> target:
            #     return 

            for n in range(i, len(candidates)):
                if n>i and candidates[n] == candidates[n-1]:
                    continue
                if curr_sum+candidates[n] > target:
                    break
                
                ans.append(candidates[n])
                dfs(curr_sum+candidates[n], n+1, ans)
                ans.pop()
            


        dfs(0,0, [])
        return res