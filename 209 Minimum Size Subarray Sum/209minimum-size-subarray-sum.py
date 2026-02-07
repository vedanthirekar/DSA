class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        min_l = float("inf")
        summ = 0
        w = float("inf")
        for r in range(n):
            summ += nums[r]
            # if summ<target:
            #     continue
            # while summ>
            while summ>=target:
                min_l = min(min_l, r - l + 1)
                summ -= nums[l]
                l+=1
                

            # if summ>=target:
            #     w = r-l+1
            # min_l = min(min_l, w)

        return 0 if min_l == float("inf") else min_l
        