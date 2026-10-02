class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero_ptr = 0
        # non_zero_ptr

        for i in range(len(nums)):
            # if zero_ptr ==-1 and nums[i]==0:
            #     zero_ptr = i
            
            

            if nums[i]:
                nums[i], nums[zero_ptr] = nums[zero_ptr], nums[i]
                zero_ptr +=1

            
        return nums

            
            

        