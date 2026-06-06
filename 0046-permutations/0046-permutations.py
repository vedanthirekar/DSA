class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # s = set()
        res = []
        n = len(nums)
        # ans = set()
        def dfs(ans, length):
            if length == n:
                res.append(ans)
                return 

            for num in nums:
                if num not in ans:
                    ans.append(num)    
                    dfs(ans[:], length+1)
                    ans.remove(num)


        dfs([], 0)
        return res