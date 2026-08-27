class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1

        while l<=h:
            mid = l+(h-l)//2

            num = nums[mid]
            if num==target:
                return mid
            elif num<target:
                l = mid+1
            else:
                h = mid-1

        return -1