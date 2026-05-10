class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        m, n = len(heights), len(heights[0])

        visitedP = [[False]*n for _ in range(m)]
        visitedA = [[False]*n for _ in range(m)]
        directions = [(0,-1), (-1,0), (0,1), (1,0)]

        def dfs(i, j, visited):
            visited[i][j] = True
            for dx, dy in directions:
                ni, nj = i+dx, j+dy
                if 0<=ni<m and 0<=nj<n and heights[ni][nj] >= heights[i][j] and not visited[ni][nj]:
                    dfs(ni, nj, visited)
        
        for i in range(m):
            if not visitedP[i][0]:
                dfs(i, 0, visitedP)
        
        for i in range(n):
            if not visitedP[0][i]:
                dfs(0, i, visitedP)
        
        for j in range(n):
            if not visitedA[m-1][j]:
                dfs(m-1, j , visitedA)
        
        for j in range(m):
            if not visitedA[j][n-1]:
                dfs(j, n-1, visitedA)
        
        result = []
        print(visitedP)
        print(visitedA)
        for i in range(m):
            for j in range(n):
                if visitedP[i][j] and visitedA[i][j]:
                    result.append([i,j])
        return result
        