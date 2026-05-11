class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])   
        i = 0
        n = len(intervals)
        new_int = intervals[0]
        # new_int.append(intervals[0])
        new_l = []
        # print (new_int)
        while i<n:
            if new_int[1]>=intervals[i][0]:
                new_int[1] = max(new_int[1], intervals[i][1])
            else:
                new_l.append(new_int)
                new_int = intervals[i]
            i += 1
        new_l.append(new_int)
        return new_l