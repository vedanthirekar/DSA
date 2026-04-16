class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        h = n-1
        m = 0 
        while l<=h:
            m = l + (h-l)//2

            if nums[l]<=nums[m]<=nums[h]:
                return nums[l]
            elif nums[l] <= nums[m] and nums[h]< nums[m]:
                l = m+1
            else:
                h = m

        return nums[m]

    