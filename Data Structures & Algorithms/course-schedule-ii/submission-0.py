class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            adj_list[v].append(u)
        
        indegree = [0] * numCourses

        for nodes in adj_list:
            for i in nodes:
                indegree[i] += 1

        queue = deque()
        for i, degree in enumerate(indegree):
            if degree == 0:
                queue.append(i)

        # Run BFS
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(result) != numCourses:
            return []
        return result