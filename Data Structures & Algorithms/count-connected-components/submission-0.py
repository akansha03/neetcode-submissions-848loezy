class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_list = [[] for _ in range(n)]

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = [False]*n

        def dfs(node):
            visited[node] = True

            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count


        