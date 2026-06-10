class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0 
        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols:
                return 0
            if grid[i][j] != 1:
                return 0
            
            grid[i][j] = -1
            return 1+dfs(i-1,j)+dfs(i+1,j)+dfs(i,j-1)+dfs(i,j+1)


        for r in range (rows):
            for c in range (cols):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    max_area = max(max_area, area)

        return max_area