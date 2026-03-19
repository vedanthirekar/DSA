class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = 1
        curr_max = 1
        global_max = max(nums)
        # n = len(nums)
        for n in nums:
            temp = curr_min*n
            curr_min = min(curr_min*n, curr_max*n, n)
            curr_max = max(curr_max*n, temp, n)

            global_max = max(curr_max, global_max)

        return global_max