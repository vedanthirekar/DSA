class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_sum = {0:1}
        summ = 0
        res = 0

        for num in nums:
            summ+= num
            diff = summ-k
            res += prefix_sum.get(diff, 0)
            prefix_sum[summ] = 1+ prefix_sum.get(summ, 0)

        return res