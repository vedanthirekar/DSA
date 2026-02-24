class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = []
        n = len(nums)
        def backtrack(i):
            if i == n:
                res.append(ans[:])
                return
            backtrack(i+1)
            ans.append(nums[i])
            backtrack(i+1)
            ans.pop()

        backtrack(0)
        return res
                