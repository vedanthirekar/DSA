class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0])
        # print(intervals)

        res = []
        n = len(intervals)
        i = 0
        while i<n: #look into edge case
            interval = intervals[i]
            while i<n-1 and interval[1]>=intervals[i+1][0]:
                interval[1] = max(interval[1], intervals[i+1][1])
                i+=1

            res.append(interval)
            i+=1

        return res

