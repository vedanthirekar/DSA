class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(ans, i):
            if len(ans) == n:
                res.append(ans[:])
                return

            for num in nums:
                if num in ans:
                    continue

                ans.append(num)
                dfs(ans, i+1)
                ans.pop()

        dfs([],0)

        return res