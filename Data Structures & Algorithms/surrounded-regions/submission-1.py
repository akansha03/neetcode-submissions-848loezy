class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        m, n = len(board), len(board[0])
        directions = [(-1,0), (0, -1), (0, 1), (1,0)]
        def dfs(i, j):

            board[i][j] = -1
            for dx, dy in directions:
                nx, ny = i+dx, j+dy
                if 0<=nx<m and 0<=ny<n: 
                    if board[nx][ny] == 'O':
                        dfs(nx, ny)
        
        # DFS on boundaries
        for i in range(n):
            if board[0][i] == 'O':
                dfs(0, i)

        for i in range(n):
            if board[m-1][i] == 'O':
                dfs(m-1, i)
        
        for j in range(m):
            if board[j][0] == 'O':
                dfs(j,0)
        
        for j in range(m):
            if board[j][n-1] == 'O':
                dfs(j, n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'



        