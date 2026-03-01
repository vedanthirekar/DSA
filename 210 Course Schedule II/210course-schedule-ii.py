from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        
        states = [UNVISITED] * numCourses
        order = []

        def dfs(node):
            if states[node] == VISITING:
                return False
            if states[node] == VISITED:
                return True

            states[node] = VISITING

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            states[node] = VISITED
            order.append(node)
            return True

        for i in range(numCourses):
            if states[i] == UNVISITED:
                if not dfs(i):
                    return []

        return order[::-1]