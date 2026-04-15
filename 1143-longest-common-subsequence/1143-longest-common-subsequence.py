class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:


        # memoization
        m = len(text1)
        n = len(text2)
        memo = {}
        def rec(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == m or j ==n:
                return 0
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + rec(i+1, j+1)
            else:
                memo[(i,j)] = max(rec(i+1, j), rec(i,j+1))

            return memo[(i,j)]
        return rec(0,0)


        # # tabulation
        # m = len(text1)
        # n = len(text2)
        # dp = [[0]*n+1 for _ in range(m)]
        
        # for i in range j



        
        
        # # normal recursion
        
        # m = len(text1)
        # n = len(text2)
        # def rec(i,j):
        #     if i == m or j ==n:
        #         return 0
        #     if text1[i] == text2[j]:
        #         return 1 + rec(i+1, j+1)
        #     else:
        #         return max(rec(i+1, j), rec(i,j+1))
        # return rec(0,0)