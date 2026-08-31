class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(x,y):
            return x**2 + y**2

        heap = []
        res = []

        for point in points:
            x,y = point
            distance = dist(x,y)

            heapq.heappush(heap, (-distance,x,y))

            if len(heap)>k:
                heapq.heappop(heap)

        
        for dist,x,y in heap:
            res.append([x,y])

        return res