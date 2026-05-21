class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """iterate over the array and try to find how farthest we can go"""
        farthest = 0
        for i in range(len(nums)):
            if i>farthest:
                return False
            farthest = max(farthest,nums[i]+i)
        return True
