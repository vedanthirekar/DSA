class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        h = len(nums)

        while l<h:
            mid = l+(h-l)//2
            
            num = nums[mid]
            if num == target:
                return mid
            if num<target:
                l+=1
            if num> target:
                h-=1

        return -1