class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = nums[0]
        for n in nums:
            if n == element:
                count += 1
            else:
                count -= 1
                if count < 0:
                    element = n
                    count = 1
        return element
        