class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """sort the array, the run a for loop for 1 variable and other 2 can be 
        found out using the 2pointer method"""

        nums.sort()
        n = len(nums)
        summ= 0
        res = []
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = n-1
            while l<r:
                summ = nums[i] + nums[l] + nums[r]

                if summ == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:  # skip duplicate lefts
                        l += 1
                    while l < r and nums[r] == nums[r+1]:  # skip duplicate rights
                        r -= 1
                elif summ<0:
                    l+=1
                else:
                    r-=1

        return res