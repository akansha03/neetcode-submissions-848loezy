class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        directions = [[0,-1], [-1,0], [0,1], [1,0]]

        def dfs(i, j, count):
            visited[i][j] = True

            for dx, dy in directions:
                new_i = i + dx
                new_j = j + dy
                if new_i<0 or new_j<0 or new_i>=m or new_j>=n or visited[new_i][new_j]:
                    continue
                elif grid[new_i][new_j] == 1:
                    count += 1
                    count = dfs(new_i, new_j, count)
            return count
                    
        max_area = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    max_area = max(max_area, dfs(i,j,1))
        return max_area
        