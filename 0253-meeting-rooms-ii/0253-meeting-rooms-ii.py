class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        
        max_count = 0
        count = 0
        starts = []
        ends = []
        # intervals.sort()
        for start, end in intervals:
            starts.append(start)
            ends.append(end)

        starts.sort()
        ends.sort()

        s = 0
        e = 0

        while s<len(intervals):

            if starts[s]<ends[e]:
                count +=1
                s+=1
            else:
                count -=1
                e+=1

            max_count = max(max_count, count)

        return max_count
