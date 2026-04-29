class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        directions = [(-1,0), (0,-1), (1,0), (0,1)]

        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j,0))

        value = 0
        while queue:
            i, j, count = queue.popleft()
            value = count
            for dx, dy in directions:
                nx, ny = i+dx, j+dy

                if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append((nx, ny, count+1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return value