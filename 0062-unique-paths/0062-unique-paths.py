class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # count = [0]
        memo = {}
        def rec (i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            if (i==m-1) or (j==n-1):
                return 1
            
            
                # count[0] += 1
            memo[(i,j)] =   rec(i+1,j) + rec(i, j+1)
            return memo[(i,j)]


        return rec(0,0)