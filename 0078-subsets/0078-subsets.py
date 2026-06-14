class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(i, ans):
            # res.append(ans[:])
            if i==n:
                res.append(ans[:])
                return 
            
            ans.append(nums[i])
            dfs(i+1, ans)
            ans.pop()
            dfs(i+1, ans)

        dfs(0, [])
        return res