class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = [0,0,0]
        for color in nums:
            c[color] +=1
            
        r,w,b = c   
        print(r, w,b)
        nums[:r] = [0]*r
        nums[r:w+r] = [1]*w
        nums[r+w:] = [2]*b

        return nums
