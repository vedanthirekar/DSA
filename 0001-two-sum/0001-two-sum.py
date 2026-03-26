class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}


        for n in range(len(nums)):
            if target-nums[n] in d1:
                return [n,d1[target-nums[n]]]
            else:
                d1[nums[n]] = n

        # return 