class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """similar to max product subarray/largest subarray. 
        can use kadane's algo here.
        using 2 variables curr max and and gloabal max"""

        curr_max = maxx = float("-inf")
        for i in nums:
            curr_max = max(0, curr_max)
            curr_max += i
            maxx = max(curr_max,maxx)

            # if curr_m
            

        return maxx