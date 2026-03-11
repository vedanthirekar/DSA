class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev = nums[0]
        n = len(nums)
        if n == 1:
            return prev
        if n == 2:
            return max(nums[0],nums[1])

        curr = max(nums[0],nums[1])

        for i in range(2,n):
            prev, curr = curr, max(nums[i]+prev, curr)

        return curr