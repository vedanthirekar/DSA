class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """My intuition is that these types of problems can be solved by greedy approach. 
        We first need to sort the intervals and we can try to interate over them"""
        "here we use min in else case becuase we need to keep the interval that ends first"
        intervals.sort()
        # print(intervals)
        prev_end = intervals[0][0]
        count = 0
        for i in intervals:
            if i[0]>=prev_end:
                prev_end = i[1]
            else:
                prev_end = min(prev_end, i[1])
                count +=1 
        return count
        
