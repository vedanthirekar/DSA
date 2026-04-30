class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = []
        m = len(board[0])
        n = len(board)
        s = set()
        for j in range(n):
            for i in range(m):
                if board[j][i] == word[0]:
                    l.append((i,j))

        

        def dfs(i,j,idx):
            if idx == len(word):
                return True

            if (i,j) in s:
                return False
            
            if i>=m or i<0 or j<0 or j>=n:
                return False

            if word[idx] != board[j][i]:
                return False
                
            s.add((i,j))

            val = dfs(i+1,j, idx+1) or dfs(i-1,j, idx+1) or dfs(i,j-1,idx+1) or dfs(i,j+1,idx+1)
            
            s.remove((i,j))

            return val

        for i,j in l:
            # s.add(i,j)
            if dfs(i,j,0):
                return True
        return False            
        