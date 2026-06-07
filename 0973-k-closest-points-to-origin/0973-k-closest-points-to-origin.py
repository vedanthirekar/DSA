class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x1,y1):
            dist = ((x1**2) + (y1**2))**(1/2)
            return dist

        heap = []
        for x,y in points:
            dist = -distance(x,y)
            if len(heap)<k:
                heapq.heappush(heap, (dist,x,y))
            else:
                heapq.heappushpop(heap, (dist,x,y))
        
        return [(x,y) for dist,x,y in heap]
            