class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()
        n = len(heights)
        m = len(heights[0])

        def dfs(ocean, i,j,prev_l):
            if i<0 or j<0 or i>=n or j>=m or (i,j) in ocean:
                return 

            if heights[i][j]<prev_l:
                return 

            ocean.add((i,j))

            dfs(ocean,i,j-1,heights[i][j])
            dfs(ocean,i,j+1,heights[i][j])
            dfs(ocean,i-1,j,heights[i][j])
            dfs(ocean,i+1,j,heights[i][j])
            
        for c in range(m):
            dfs(pacific, 0, c, heights[0][c])
            dfs(atlantic,n-1,c,heights[n-1][c])

        for r in range(n):
            dfs(pacific, r, 0, heights[r][0])
            dfs(atlantic, r, m-1, heights[r][m-1])

        # for r,c in pacific: # this leads to add to set while interating over it. which cause error
        #     dfs(pacific, r, c, 0)

        # for r,c in atlantic:
        #     dfs(atlantic, r, c, 0)

        return [(r,c) for (r,c) in pacific if (r,c) in atlantic]
            