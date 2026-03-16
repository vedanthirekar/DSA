class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest = float("inf")
        # target = 
        for i in range(n):
            l = i+1
            r = n-1
            while l<r:
                summ =  nums[i]+nums[l]+nums[r]
                if summ == target:
                    return target
                else:    
                    if abs(closest-target) > abs(summ-target):
                            closest = summ
                    if summ>target:
                        r-=1
                    else:
                        l+=1
        return closest


