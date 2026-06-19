class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort()
        def dfs(i, ans):
            if i ==n:
                res.add(tuple(ans))
                return 

            ans.append(nums[i])
            dfs(i+1, ans)
            ans.pop()
            dfs(i+1, ans)

        dfs(0,[])
        return list(res)