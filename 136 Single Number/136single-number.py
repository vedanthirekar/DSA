class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # li = [nums[0]]
        a = nums[0]
        n = len(nums)
        for i in range(1,n):
            a = a^nums[i]

        return a
