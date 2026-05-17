class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        
        adj_list = [[] for _ in range(n)]

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = [False]*n
        
        def dfs(node, parent):
            visited[node] = True
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):
                        return True
                elif parent != neighbor:
                    return True
            return False
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                if dfs(i, -1) or count > 1:
                    return False
        return True

            






