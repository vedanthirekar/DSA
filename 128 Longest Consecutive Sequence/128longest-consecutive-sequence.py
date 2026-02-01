class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      
        max_seq = 0
        # curr_seq = 0
        s = set(nums)
        
        for n in s:
            if n-1 not in s:

                curr_seq = 1
                while n+1 in s:
                    n +=1
                    curr_seq +=1
                max_seq = max(curr_seq, max_seq)

        return max_seq