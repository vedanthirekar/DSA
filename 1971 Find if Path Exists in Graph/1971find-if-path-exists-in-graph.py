class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #using stack
        graph = defaultdict(list)
        stk = []
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        stk.append(source)
        seen = set()
        seen.add(source)

        while stk:
            node = stk.pop()
            if node ==destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stk.append(neighbor)

        return False
