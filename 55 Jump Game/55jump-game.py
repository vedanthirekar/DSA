class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        dp = [0]*(n)
        # dp[0] = nums[0]
        
        for i in range(0,n):
            dp[i] = nums[i]+i

        # print(dp)
        i = 1
        
        while i<n:
            # if i
            j = i-1
            while j>=0:
                if i<=dp[j]:
                    i = dp[j]+1
                    break
                else:
                     j-= 1
            if j<0:
                return False

        return True