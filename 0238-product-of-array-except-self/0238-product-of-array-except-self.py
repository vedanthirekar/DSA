class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [1]*n
        prod = 1
        r = [1]*n
        res = [1]*n
        for i in range(1, n):
            prod = prod*nums[i-1]
            l[i] = prod
        # print(l)
        
        prod = 1
        for i in range(n-2,-1,-1):
            prod = prod*nums[i+1]
            r[i] = prod
        # print(r)

        for i in range(n):
            res[i] = r[i]*l[i]

        return res