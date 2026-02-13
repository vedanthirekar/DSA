import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        min_h = []
        l = []
        for key,v in count.items():
            if len(min_h)<k:
                heapq.heappush(min_h, (v,key))
            else:
                heapq.heappushpop(min_h, (v,key))

        return [h[1] for h in min_h]