class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        j = 0
        for i in range(len(nums)):
            

            if nums[i] in seen:
                continue
            else:
                nums[j] = nums[i]
                j+=1
                seen.add(nums[i])

        return j