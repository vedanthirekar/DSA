class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """we can have two arrays prod of right and prod of left to save us from 
        recomputing the product everytime. then we multiply these with eachother. 
        To optimize this more, we can sequentially do left first and then right or vice-versa  
        """

        n = len(nums)
        res = [1]*n
        prod = 1
        for i in range(1,n):
            res[i] = res[i-1]*nums[i-1]

        for i in range(n-2,-1,-1):
            prod = prod*nums[i+1]
            res[i] = res[i]*prod
        
        return res