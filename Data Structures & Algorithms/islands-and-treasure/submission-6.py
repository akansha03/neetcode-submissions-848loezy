class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m, n = len(grid), len(grid[0])
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        while queue:
            i, j = queue.popleft()

            for dx, dy in directions:
                nx, ny = i+dx, j+dy

                if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 2147483647:
                    grid[nx][ny] = 1 + grid[i][j]
                    queue.append((nx, ny))
        


