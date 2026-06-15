class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        # m = len(board[0])

        for r in range(n):
            visit = set()
            for c in range(n):
                if board[r][c] == ".":
                    continue
                if board[r][c] in visit:
                    return False
                visit.add(board[r][c])

        for c in range(n):
            visit = set()
            for r in range(n):
                if board[r][c] == ".":
                    continue
                if board[r][c] in visit:
                    return False
                visit.add(board[r][c])

        starts = [(0,0), (0,3),(0,6),(3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]

        for i,j in starts:
            visit = set()
            for r in range(i,i+3):
                for c in range(j,j+3):
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in visit:
                        return False
                    visit.add(board[r][c])

        return True