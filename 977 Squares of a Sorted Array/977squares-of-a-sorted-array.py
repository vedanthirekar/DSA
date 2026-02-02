class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]

        l = 0
        r = len(nums)-1
        arr = []
        while l<=r:
            if nums[r]>nums[l]:
                arr.append(nums[r])
                r -=1
            else:
                arr.append(nums[l])
                l+=1
        arr.reverse()
        return arr
        