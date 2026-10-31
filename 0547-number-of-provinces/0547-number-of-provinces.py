class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        res = 0
        n = len(isConnected)
        visited = [False]*n

        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] ==1:
                    graph[i].append(j)

        def dfs(node):
            if visited[node] == True:
                return False

            visited[node] = True
            for nei in graph[node]:
                dfs(nei)
            return True
            

        for node in graph:
            if dfs(node):
                res+=1

        return res