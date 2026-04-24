class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxx = 0
        for i in s:
            count = 1
            if i-1 not in s:
                while i+1 in s:
                    count +=1
                    i+=1
                maxx = max(count, maxx)

        return maxx