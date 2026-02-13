import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        l  = []
        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            distance = math.sqrt(x1*x1 + y1*y1)

            if len(heap)<k:
                heapq.heappush(heap, (-distance, points[i]))
            else:
                heapq.heappushpop(heap, (-distance, points[i]))

        
        for i in range(k):
            l.append(heapq.heappop(heap)[1])

        return l