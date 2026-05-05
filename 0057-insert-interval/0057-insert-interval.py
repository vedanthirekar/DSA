class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """simulate with interating over the intervals. different conditions apply for each case of intersection"""
        new = []
        for n, i in enumerate(intervals):
            if i[1]<newInterval[0]:
                new.append(i)
            elif i[0]>newInterval[1]:
                return new + [newInterval] + intervals[n:]
            else:
                newInterval[0] = min(newInterval[0],i[0])
                newInterval[1] = max(newInterval[1],i[1])

        return new+[newInterval]