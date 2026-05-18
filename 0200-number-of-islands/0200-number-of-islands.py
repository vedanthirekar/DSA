class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """we iterate through all of the elements in the grid. If we find a 1 i.e. island,
        we go on checking other surrounding elements using dfs and simultaneously mark them 0 so that these do
        not get visited again. 
        """
        n = len(grid)
        m = len(grid[0])

        def dfs(i,j):
            if i>=n or i<0 or j<0 or j>=m:
                return 
            if grid[i][j] =="0":
                return

            grid[i][j] = "0"
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)
            return

        counter = 0
        for i in range (n):
            for j in range (m):
                if grid[i][j] == "1":
                    counter +=1
                    dfs(i,j)
        return counter