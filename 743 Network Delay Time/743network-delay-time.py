class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,time in times:
            graph[u].append((v,time))

        min_heap = [(0,k)]
        dic = {}

        while min_heap:
            d1, i = heapq.heappop(min_heap)
            if i in dic:
                continue
            dic[i] = d1

            for nei,nei_time in graph[i]:
                if nei not in dic:
                    heapq.heappush(min_heap, (d1+nei_time,nei))

        if len(dic)<n:
            return -1
        else:
            return max(dic.values())