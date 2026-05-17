class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if numCourses == 1:
            return True
        
        adj_list = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj_list[v].append(u)
        
        visited = [False] * numCourses
        pathVisited = [False] * numCourses

        def dfs(node):
            visited[node] = True
            pathVisited[node] = True

            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif pathVisited[neighbor]:
                    return True
            pathVisited[node] = False
            return False


        for i in range(numCourses):
            if dfs(i):
                return False
        return True

        