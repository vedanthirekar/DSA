class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = 0
        maxx = 0
        for i in range(k):
            maxx += nums[i]
            summ +=nums[i]
            

        

        for r in range(k,len(nums)):
            summ += nums[r]
            summ -= nums[r-k]

            maxx = max(maxx, summ)

        return maxx/k