class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        min_heap = [(0,0)]
        n = len(points)
        seen = set()
        cost = 0

        while len(seen)<n:
            d,i = heapq.heappop(min_heap)
            if i in seen:
                continue
            seen.add(i)
            cost = cost+d
            xi,yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj,yj = points[j]
                    nei_dist = abs(xj-xi) + abs (yj-yi)
                    heapq.heappush(min_heap,(nei_dist,j))

        return cost


