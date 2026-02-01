class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        h1 = set()
        for i in range(9):
            h = set()
            for j in range(9):
                if board[i][j] in h:
                    return False
                elif board[i][j] != '.':
                    h.add(board[i][j])
        
        for i in range(9):
            h = set()
            for j in range(9):
                if board[j][i] in h:
                    return False
                elif board[j][i] != '.':
                    h.add(board[j][i])

        starts = [(0,0),(0,3),(0,6),
        (3,0),(3,3),(3,6),
        (6,0),(6,3),(6,6)]

        for i,j in starts:
            h = set()
            for r in range(i,i+3):
                for c in range(j,j+3):
                    item = board[r][c]
                    if item in h:
                        return False
                    elif item != '.':
                        h.add(item)

        return True