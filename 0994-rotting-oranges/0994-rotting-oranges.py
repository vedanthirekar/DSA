class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def helper(r,c):
            if r>=0 and c>=0 and r<rows and c<cols and grid[r][c] == 1:
                grid[r][c] = 2
                queue.append((r,c))

            
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        seen = set()
        total_orange = 0
        time = 0


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    seen.add((r,c))
                    queue.append((r,c))
                    total_orange +=1

                if grid[r][c] ==1:
                    total_orange +=1
        if total_orange == 0:
            return 0
        while queue:
            time+=1
            for _ in range(len(queue)):
                r,c = queue.popleft()
                seen.add((r,c))
                helper(r-1,c)
                helper(r+1,c)
                helper(r,c+1)
                helper(r,c-1)


        if len(seen)==total_orange:
            return time-1
        else:
            return -1



