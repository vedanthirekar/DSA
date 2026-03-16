class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        s = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            l = i+1
            r = n-1
            while l<r:
                if nums[l]+nums[r] == target:
                    s.append([nums[i],nums[l],nums[r]])
                    # break
                    l +=1
                    r -=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif nums[l]+nums[r]>target:
                    r -=1
                else:
                    l+=1
        return s
            