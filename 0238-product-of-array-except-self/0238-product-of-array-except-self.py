class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        l = [1]* n
        r = [1]* n

        prod = 1

        for i in range(1, n):
            prod = nums[i-1]* prod
            l[i] = prod

        # print(l)

        prod = 1

        for i in range(n-2, -1, -1):
            prod = nums[i+1]*prod
            r[i] = prod

        print(r)

        for i in range(n):
            nums[i] = r[i]*l[i]

        return nums 