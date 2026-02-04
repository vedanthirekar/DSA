class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l = 0
        h = m*n-1

        while l<=h:
            mid = l + (h-l)//2
            r = mid//m
            c = mid%m

            if matrix[r][c] == target:
                return True
            elif matrix[r][c]<target:
                l = mid+1
            else: 
                h = mid-1

        return False

        