class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        border = []

        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            if board[r][c] != "O":
                return 
            # if board[r][c] == "O":
            
            board[r][c] = "-"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
            return 


        for r in range(rows):
            border.append([r,0])
            border.append([r,cols-1])

        for c in range(cols):
            border.append([0,c])
            border.append([rows-1,c])

        print(border)

        for r,c in border:
            if board[r][c] == "O":
                dfs(r,c) 

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "-":
                    board[r][c] = "O"

        