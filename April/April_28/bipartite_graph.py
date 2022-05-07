class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [0]*n
        
        for node in range(n):
            if visited[node] == 0:
                visited[node] = 1
                q = deque()
                q.append(node)
                while q:
                    curr = q.popleft()
                    for adj in graph[curr]:
                        if visited[adj] == 0:
                            visited[adj] = -visited[curr]
                            q.append(adj)
                        elif visited[adj] == visited[curr]:
                            return False
                    
        return True
