class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)
        m= len(matrix[0])
        l= 0
        h = m*n -1

        while l<=h:
            mid = l + (h-l)//2
            row = mid//m
            col = mid%m

            if target == matrix[row][col]:
                return True
            elif target <matrix[row][col]:
                h= mid-1
            else:
                l = mid+1

        return False