class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        adj_list = [[] for _ in range(n+1)]
        

        def dfs(node, parent):
            if visit[node]:
                return True
            visit[node] = True
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                elif dfs(neighbor, node):
                    return True
            return False

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            visit = [False]*(n+1)
           
            if dfs(u, -1):
                return [u,v]
        return []