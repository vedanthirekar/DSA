class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        count = 0
        fresh = 0
        # seen = set()

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            nonlocal fresh
            if r>=0 and c>=0 and c<cols and r<rows and grid[r][c] == 1:
                grid[r][c] = 2
                queue.append((r,c))
                fresh -=1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    # seen.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        while queue and fresh> 0:
            l = len(queue)
            count +=1
            for i in range(l):
                r,c = queue.popleft()
                bfs(r,c-1)
                bfs(r,c+1)
                bfs(r-1,c)
                bfs(r+1,c)


        return count if not fresh else -1

        