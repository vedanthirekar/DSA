class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        diff = float('inf')
        for n in nums:
            if abs(n)<abs(diff):
                diff = n
            if abs(n)==abs(diff):
                diff = max(n, diff)

        return diff
            

