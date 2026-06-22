class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # heap = []
        # for i in range(len(stones)):
        #     s[i] = 
        # stones = stones*-1
        new_stones = [-x for x in stones]
        heapq.heapify(new_stones)

        while len(new_stones)>1:
            a = -heapq.heappop(new_stones)
            b = -heapq.heappop(new_stones)
            if a > b:
                heapq.heappush(new_stones, -a+b)
                
        return 0 if not new_stones else -new_stones[0]