class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        h = n-1

        while l<=h:
            m = l + (h-l)//2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                h = m-1
            else:
                return m
        if nums[m]<target:
            return m+1
        else:
            return m