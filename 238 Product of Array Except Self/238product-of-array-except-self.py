class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 1
        r = 1
        llist = [0]*n
        rlist = [0]*n
        for i in range(n):
            j = n-i-1
            llist[i] = l
            rlist[j] = r
            l = l*nums[i]
            r = r*nums[j]

        return [l*r for l,r in zip(llist,rlist)]
            


        