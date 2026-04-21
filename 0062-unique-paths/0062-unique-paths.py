class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def unique(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == m-1 or j ==n-1:
                memo[(i,j)] = 1
            else:
                memo[(i,j)] =  unique(i,j+1) + unique(i+1,j)
            return memo[(i,j)]
        return unique(0,0)