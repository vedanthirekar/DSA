class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = 0
        li = []
        while i < m and j < n:
            for k in range(i, m):
                li.append(matrix[j][k])
            j += 1

            for k in range(j, n):
                li.append(matrix[k][m - 1])
            m -= 1

            if j < n:
                for k in range(m - 1, i - 1, -1):
                    li.append(matrix[n - 1][k])
                n -= 1

            if i < m:
                for k in range(n - 1, j - 1, -1):
                    li.append(matrix[k][i])
                i += 1
        return li



            

