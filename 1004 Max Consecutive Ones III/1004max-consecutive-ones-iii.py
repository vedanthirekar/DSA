class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        # r = 0

        zeros = 0
        maxx = 0
        # win = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros +=1

            while zeros>k:
                
                if nums[l] ==0:
                    zeros -=1
                l +=1
            w = r-l+1
            maxx = max(maxx,w)

        return maxx

