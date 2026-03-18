class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # s = set()
        n = len(nums)
        i = 1
        j = 1
        while i<n:
            if nums[i] != nums[i-1]:
                # nums[i] = nums[n-1]
                # i += 1
                nums[j] = nums[i]
                j += 1
                i+=1
                # n -=1

            else:
                # s.add(nums[i])
                i +=1 
        # nums.sort()
        return j