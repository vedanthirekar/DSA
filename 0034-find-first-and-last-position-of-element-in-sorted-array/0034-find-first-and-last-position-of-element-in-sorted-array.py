class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        

        def binarySearch(arr, target):
            l = 0
            r = len(arr)

            while l<r:

                mid = l+(r-l)//2
                if arr[mid]<target:
                    l = mid+1

                else:
                    r = mid

            return l
            # return index

        start = binarySearch(nums, target)

        # print(start)
        if start == len(nums) or nums[start]!= target:
            return [-1,-1]

        return [start, binarySearch(nums,target+1)-1]