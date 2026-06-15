class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo  = {}
        def dfs(i):
            # if s[i] and s[i] == 0:
            #     return 0

            if i<n and s[i] == "0":
                return 0
            if i >= n-1:
                return 1

            if i in memo:
                return memo[i]

            # if i>=n:
            #     return 1
            
            

            ways = dfs(i+1)

            if i<n-1 and s[i] == "1":
                ways += dfs(i+2)

            if i<n-1 and s[i] == "2":
                if s[i+1] and s[i+1] in "0123456":
                    ways+= dfs(i+2)
            memo[i] = ways
            return ways



        return dfs(0)